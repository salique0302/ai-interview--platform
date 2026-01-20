from fastapi import FastAPI

# Application factory
def create_app() -> FastAPI:
    app = FastAPI(
        title="AI Interview Platform API",
        description="Backend system for AI-powered interview and resume feedback platform",
        version="0.1.0"
    )

    @app.get("/health")
    def health_check():
        return {"status": "healthy"}

    return app


app = create_app()
