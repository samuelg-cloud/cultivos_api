from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database.conexion import get_db
from app.schemas.esquemas import (
    UsuarioCrear, UsuarioActualizar, UsuarioRespuesta,
    CultivoCrear, CultivoActualizar, CultivoRespuesta
)
from app.services import servicio

router_usuarios = APIRouter(prefix="/usuarios", tags=["Usuarios"])
router_cultivos = APIRouter(prefix="/cultivos", tags=["Cultivos"])

@router_usuarios.post("/", response_model=UsuarioRespuesta, status_code=201)
def crear_usuario(datos: UsuarioCrear, db: Session = Depends(get_db)):
    return servicio.registrar_usuario(db, datos)

@router_usuarios.get("/", response_model=List[UsuarioRespuesta])
def listar_usuarios(db: Session = Depends(get_db)):
    return servicio.consultar_usuarios(db)

@router_usuarios.get("/{usuario_id}", response_model=UsuarioRespuesta)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return servicio.consultar_usuario_por_id(db, usuario_id)

@router_usuarios.put("/{usuario_id}", response_model=UsuarioRespuesta)
def editar_usuario(usuario_id: int, datos: UsuarioActualizar, db: Session = Depends(get_db)):
    return servicio.actualizar_usuario(db, usuario_id, datos)

@router_usuarios.delete("/{usuario_id}")
def borrar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return servicio.eliminar_usuario(db, usuario_id)

@router_cultivos.post("/", response_model=CultivoRespuesta, status_code=201)
def crear(datos: CultivoCrear, db: Session = Depends(get_db)):
    return servicio.registrar_cultivo(db, datos)

@router_cultivos.get("/", response_model=List[CultivoRespuesta])
def listar(tipo: Optional[str] = Query(None), db: Session = Depends(get_db)):
    return servicio.consultar_cultivos(db, tipo)

@router_cultivos.get("/{cultivo_id}", response_model=CultivoRespuesta)
def obtener(cultivo_id: int, db: Session = Depends(get_db)):
    return servicio.consultar_por_id(db, cultivo_id)

@router_cultivos.put("/{cultivo_id}", response_model=CultivoRespuesta)
def editar(cultivo_id: int, datos: CultivoActualizar, db: Session = Depends(get_db)):
    return servicio.actualizar_cultivo(db, cultivo_id, datos)

@router_cultivos.delete("/{cultivo_id}")
def borrar(cultivo_id: int, db: Session = Depends(get_db)):
    return servicio.eliminar_cultivo(db, cultivo_id)
