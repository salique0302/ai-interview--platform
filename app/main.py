from fastapi import FastAPI

from app.db.base import Base
from app.db.session import engine


def create_app() -> FastAPI:
    app = FastAPI(
        title="AI Interview Platform API",
        description="Backend system for AI-powered interview and resume feedback platform",
        version="0.1.0"
    )

    @app.on_event("startup")
    def startup_event():
        Base.metadata.create_all(bind=engine)

    @app.get("/health")
    def health_check():
        return {"status": "healthy"}

    return app


app = create_app()
