from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr

class UsuarioCrear(BaseModel):
    nombre: str
    correo: EmailStr
    contrasena: str

class UsuarioActualizar(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None
    contrasena: Optional[str] = None

class UsuarioRespuesta(BaseModel):
    id: int
    nombre: str
    correo: EmailStr

    class Config:
        from_attributes = True

class CultivoCrear(BaseModel):
    nombre_cultivo: str
    tipo_cultivo: str
    area_sembrada: float
    fecha_siembra: date
    fecha_estimada_cosecha: date

class CultivoActualizar(BaseModel):
    nombre_cultivo: Optional[str] = None
    tipo_cultivo: Optional[str] = None
    area_sembrada: Optional[float] = None
    fecha_siembra: Optional[date] = None
    fecha_estimada_cosecha: Optional[date] = None

class CultivoRespuesta(CultivoCrear):
    id: int

    class Config:
        from_attributes = True
