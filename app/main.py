from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from pathlib import Path
from app.core.config import settings
from app.db.session import  Base, engine
from app.api.routes.health import router as health_router
from app.api.routes.auth import router as auth_router
from app.api.routes.predict import router as predict_router
from app.core.logging import setup_logging
import logging
import time
import pickle

MODEL_PATH = Path("app/ml/model.pkl")

setup_logging()
logger = logging.getLogger("app")
@asynccontextmanager
async def lifespan(app: FastAPI):
    with MODEL_PATH.open("rb") as f:
        app.state.model = pickle.load(f)

    yield

app = FastAPI(lifespan=lifespan)
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = round((time.time() - start_time) * 1000, 2)
    logger.info (
        "%s %s status=%s duration_ms=%s",
        request.method,
        request.url.path,
        response.status_code,
        duration
    )

    return response
app.include_router(predict_router)
app.include_router(health_router)
app.include_router(auth_router)