from loguru import logger

from app.models import AlertmanagerWebhook
from app.routing import get_channels_for_severity
from app.formatter import format_alert
from app.notifiers import registry
from app.state import record_alert


def handle_webhook(webhook: AlertmanagerWebhook) -> None:
    for alert in webhook.alerts:
        severity = alert.labels.get("severity", "default")
        channels = get_channels_for_severity(severity)
        message = format_alert(alert)

        record_alert(
            alert_name=alert.labels.get("alertname", "UnknownAlert"),
            severity=severity,
            status=alert.status,
            summary=alert.annotations.get("summary") or alert.annotations.get("description", ""),
            channels=channels,
        )

        for channel in channels:
            send_fn = registry.get(channel)
            if send_fn is None:
                logger.warning(f"No notifier registered for channel '{channel}'")
                continue
            try:
                send_fn(message)
            except Exception as e:
                logger.error(f"Failed to send alert via {channel}: {e}")