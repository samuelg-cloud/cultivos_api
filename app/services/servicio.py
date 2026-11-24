from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.repositories import repositorio
from app.schemas.esquemas import UsuarioCrear, UsuarioActualizar, CultivoCrear, CultivoActualizar

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashear_contrasena(contrasena: str) -> str:
    return pwd_context.hash(contrasena)

def registrar_usuario(db: Session, datos: UsuarioCrear):
    if not datos.nombre.strip() or not datos.contrasena.strip():
        raise HTTPException(status_code=400, detail="Nombre y contraseña son obligatorios")
    if repositorio.obtener_usuario_por_correo(db, datos.correo):
        raise HTTPException(status_code=400, detail="El correo ya está registrado")
    hash_pw = hashear_contrasena(datos.contrasena)
    return repositorio.crear_usuario(db, datos.nombre.strip(), datos.correo, hash_pw)

def consultar_usuarios(db: Session):
    return repositorio.listar_usuarios(db)

def consultar_usuario_por_id(db: Session, usuario_id: int):
    usuario = repositorio.obtener_usuario_por_id(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

def actualizar_usuario(db: Session, usuario_id: int, datos: UsuarioActualizar):
    usuario_db = consultar_usuario_por_id(db, usuario_id)
    cambios = datos.model_dump(exclude_unset=True)
    if "correo" in cambios and cambios["correo"] != usuario_db.correo:
        if repositorio.obtener_usuario_por_correo(db, cambios["correo"]):
            raise HTTPException(status_code=400, detail="El correo ya está en uso")
    if "contrasena" in cambios and cambios["contrasena"]:
        cambios["contrasena"] = hashear_contrasena(cambios["contrasena"])
    return repositorio.actualizar_usuario(db, usuario_db, cambios)

def eliminar_usuario(db: Session, usuario_id: int):
    usuario_db = consultar_usuario_por_id(db, usuario_id)
    repositorio.eliminar_usuario(db, usuario_db)
    return {"mensaje": "Usuario eliminado"}

def registrar_cultivo(db: Session, datos: CultivoCrear):
    if datos.area_sembrada <= 0:
        raise HTTPException(status_code=400, detail="El área sembrada debe ser mayor a 0")
    if datos.fecha_estimada_cosecha < datos.fecha_siembra:
        raise HTTPException(status_code=400, detail="La fecha de cosecha no puede ser anterior a la de siembra")
    return repositorio.crear(db, datos)

def consultar_cultivos(db: Session, tipo: str = None):
    return repositorio.listar(db, tipo)

def consultar_por_id(db: Session, cultivo_id: int):
    cultivo = repositorio.obtener_por_id(db, cultivo_id)
    if not cultivo:
        raise HTTPException(status_code=404, detail="Cultivo no encontrado")
    return cultivo

def actualizar_cultivo(db: Session, cultivo_id: int, datos: CultivoActualizar):
    cultivo_db = consultar_por_id(db, cultivo_id)
    return repositorio.actualizar(db, cultivo_db, datos)

def eliminar_cultivo(db: Session, cultivo_id: int):
    cultivo_db = consultar_por_id(db, cultivo_id)
    repositorio.eliminar(db, cultivo_db)
    return {"mensaje": "Cultivo eliminado"}
