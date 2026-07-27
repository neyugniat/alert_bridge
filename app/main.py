from fastapi import FastAPI
from app.api.webhook import router 

app = FastAPI(
    title="Alert Bridge",
    version="0.1.0",
)

app.include_router(router, prefix="/api")

@app.get('/')
async def root():
    return {"status": "ok"}
