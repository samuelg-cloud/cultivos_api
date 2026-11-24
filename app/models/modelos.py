from sqlalchemy import Column, Integer, String, Float, Date
from app.database.conexion import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)
    correo = Column(String(120), unique=True, index=True, nullable=False)
    contrasena = Column(String(255), nullable=False)

class Cultivo(Base):
    __tablename__ = "cultivos"

    id = Column(Integer, primary_key=True, index=True)
    nombre_cultivo = Column(String(100), nullable=False)
    tipo_cultivo = Column(String(50), nullable=False)
    area_sembrada = Column(Float, nullable=False)
    fecha_siembra = Column(Date, nullable=False)
    fecha_estimada_cosecha = Column(Date, nullable=False)
