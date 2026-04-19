from fastapi import FastAPI
from app.routes.metrics import router as metrics_router

app = FastAPI()

app.include_router(metrics_router)

#rota testar api
@app.get("/")
def status():
    return {"status":"ok","message":"DevWatch rodando"}




