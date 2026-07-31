from app.notifiers.telegram import send_telegram
from app.notifiers.discord import send_discord

registry = {
    "telegram": send_telegram,
    "discord": send_discord,
}