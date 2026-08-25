from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine
from app.routers import auth,jobs


app = FastAPI(
    title="RecruitFlow API",
    description="Backend API for a recruitment platform",
    version="1.0.0"
)


app.include_router(auth.router)
app.include_router(jobs.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to RecruitFlow API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

    return {
        "database": "connected",
        "result": result.scalar()
    }