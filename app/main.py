from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="External Source Load",
    version="1.0.0",
)

app.include_router(router.api_router)
