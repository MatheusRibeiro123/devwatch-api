from fastapi import FastAPI
from app.routes.metrics_route import router as metrics_router
from app.database import engine,Base
from app.models.metrics_model import Metrics
from app.services.monitor import start_monitor

app = FastAPI()

@app.on_event("startup")
def startup():
    start_monitor()

app.include_router(metrics_router)

Base.metadata.create_all(bind=engine)

#rota testar api
@app.get("/")
def status():
    return {"status":"ok","message":"DevWatch rodando"}




