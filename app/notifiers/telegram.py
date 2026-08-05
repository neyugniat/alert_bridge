import httpx
from loguru import logger

from app.config import Settings

TELEGRAM_API_URL = "https://api.telegram.org/bot{token}/sendMessage"

def send_telegram(message: str) -> None:
    if not Settings.telegram_bot_token or not Settings.telegram_chat_id:
        logger.warning("Telegram not configured - skipping notification")
        return

    url = TELEGRAM_API_URL.format(token=Settings.telegram_bot_token)
    payload = {
        "chat_id": Settings.telegram_chat_id,
        "text": message,
    }

    response = httpx.post(url, json=payload)
    response.raise_for_status()