from sqlalchemy.orm import Session
from app.models.modelos import Usuario, Cultivo
from app.schemas.esquemas import UsuarioCrear, UsuarioActualizar, CultivoCrear, CultivoActualizar

def crear_usuario(db: Session, nombre: str, correo: str, contrasena_hash: str):
    nuevo = Usuario(nombre=nombre, correo=correo, contrasena=contrasena_hash)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def listar_usuarios(db: Session):
    return db.query(Usuario).all()

def obtener_usuario_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def obtener_usuario_por_correo(db: Session, correo: str):
    return db.query(Usuario).filter(Usuario.correo == correo).first()

def actualizar_usuario(db: Session, usuario_db: Usuario, datos_dict: dict):
    for k, v in datos_dict.items():
        setattr(usuario_db, k, v)
    db.commit()
    db.refresh(usuario_db)
    return usuario_db

def eliminar_usuario(db: Session, usuario_db: Usuario):
    db.delete(usuario_db)
    db.commit()

def crear(db: Session, datos: CultivoCrear):
    nuevo = Cultivo(**datos.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def listar(db: Session, tipo: str = None):
    q = db.query(Cultivo)
    if tipo:
        q = q.filter(Cultivo.tipo_cultivo.ilike(f"%{tipo}%"))
    return q.all()

def obtener_por_id(db: Session, cultivo_id: int):
    return db.query(Cultivo).filter(Cultivo.id == cultivo_id).first()

def actualizar(db: Session, cultivo_db: Cultivo, datos: CultivoActualizar):
    for k, v in datos.model_dump(exclude_unset=True).items():
        setattr(cultivo_db, k, v)
    db.commit()
    db.refresh(cultivo_db)
    return cultivo_db

def eliminar(db: Session, cultivo_db: Cultivo):
    db.delete(cultivo_db)
    db.commit()
