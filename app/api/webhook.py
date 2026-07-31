from fastapi import APIRouter
from loguru import logger

from app.models import AlertmanagerWebhook
from app.dispatch import handle_webhook

router = APIRouter()


@router.post("/webhook")
async def webhook(payload: AlertmanagerWebhook):
    logger.info(f"Received {len(payload.alerts)} alert(s) from Alertmanager")
    handle_webhook(payload)
    return {"status": "received", "alerts": len(payload.alerts)}