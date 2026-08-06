import httpx
from loguru import logger

from app.config import Settings

def send_discord(message: str) -> None:
    logger.info(f"[discord placeholder] would send: {message}")