from pathlib import Path
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse

from app.state import get_alerts

router = APIRouter()

TEMPLATE_PATH = Path(__file__).resolve().parent.parent / "templates" / "dashboard.html"


@router.get("/api/alerts")
async def api_alerts():
    return JSONResponse(get_alerts())


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    return TEMPLATE_PATH.read_text()