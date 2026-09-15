from fastapi import FastAPI

from routers.projects import router as projects_router


app = FastAPI(
    title="DevFlow AI API",
    description="AI-powered CI/CD platform",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "DevFlow AI"
    }


app.include_router(projects_router)