from fastapi import APIRouter
from app.routes import process_load

api_router = APIRouter()

api_router.include_router(process_load.router, prefix="/load", tags=["ELT Load Operations"])
