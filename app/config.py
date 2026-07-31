import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    telegram_bot_token: str | None = os.getenv("TELEGRAM_BOT_TOKEN")
    telegram_chat_id: str | None = os.getenv("TELEGRAM_CHAT_ID")
    discord_webhook_url: str | None = os.getenv("DISCORD_WEBHOOK_URL")