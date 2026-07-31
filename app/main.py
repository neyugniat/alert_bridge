import uvicorn
from fastapi import FastAPI
from app.api.webhook import router
from app.api.dashboard import router as dashboard_router

app = FastAPI(
    title="Alert Bridge",
    version="0.1.0",
)

app.include_router(router, prefix="/api")
app.include_router(dashboard_router)


@app.get("/healthz")
async def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=9999, reload=True)