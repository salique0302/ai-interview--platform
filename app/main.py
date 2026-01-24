from fastapi import FastAPI
from app.db import models
from app.db.base import Base
from app.db.session import engine


def create_app() -> FastAPI:
    app = FastAPI(
        title="AI Interview Platform API",
        description="Backend system for AI-powered interview and resume feedback platform",
        version="0.1.0"
)

    from app.api.routes import auth
    app.include_router(auth.router, prefix="/auth", tags=["Auth"])

    @app.on_event("startup")
    def startup_event():
        Base.metadata.create_all(bind=engine)

    @app.get("/health")
    def health_check():
        return {"status": "healthy"}

    @app.get("/")
    def root():
        return {"message": "AI Interview Platform API running"}

    

    return app


app = create_app()
