from fastapi import FastAPI

from app.api.routes_auth import router as auth_router

app = FastAPI(title="Simulador Previdenciário API")

@app.get("/")
def read_root():
    return {"message": "API do Simulador Previdenciário está online"}

app.include_router(auth_router)