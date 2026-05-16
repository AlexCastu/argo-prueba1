from fastapi import FastAPI

app = FastAPI(title="argo-prueba1")


@app.get("/")
def leer_raiz() -> dict[str, str]:
    return {"message": "Hola mundo"}
