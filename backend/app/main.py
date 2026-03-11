from fastapi import FastAPI

app = FastAPI(title="Simulador Previdenciário API")

@app.get("/")
def read_root():
    return {"message": "API do Simulador Previdenciário está online"}