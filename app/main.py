from fastapi import FastAPI
from app.database.conexion import engine, Base
from app.models import modelos
from app.routes.rutas import router_usuarios, router_cultivos

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Usuarios y Cultivos Agrícolas")
app.include_router(router_usuarios)
app.include_router(router_cultivos)
