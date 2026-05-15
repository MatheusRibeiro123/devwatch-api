from fastapi import FastAPI
from app.routes.metrics_route import router as metrics_router
from app.database import engine,Base
from app.models.metrics_model import Metrics
from app.services.monitor import start_monitor
from app.handles.exceptions_handles import register_handlers
import logging
from fastapi.middleware.cors import CORSMiddleware


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"],
)

app.include_router(metrics_router)

register_handlers(app)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    start_monitor()
    logger.info("Aplicação iniciada e monitoramento de métricas iniciado.")


#rota testar api
@app.get("/")
def status():
    return {"status":"ok","message":"DevWatch rodando"}




