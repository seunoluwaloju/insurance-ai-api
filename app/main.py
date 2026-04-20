from fastapi import FastAPI
from app.core.config import settings
from app.db.session import  Base, engine
from app.api.routes.health import router as health_router
from app.api.routes.auth import router as auth_router
from app.api.routes.predict import router as predict_router

app = FastAPI(title=settings.app_name)
app.include_router(predict_router)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(health_router)
app.include_router(auth_router)