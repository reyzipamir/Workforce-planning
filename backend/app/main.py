
from fastapi import FastAPI
from .routers import planning

app = FastAPI(title="Adaptive Workforce Control Tower")

app.include_router(planning.router, prefix="/plan", tags=["Planning"])

@app.get("/")
def root():
    return {"status": "ok"}
