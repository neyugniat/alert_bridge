from collections import deque
from datetime import datetime, timezone

MAX_ALERTS = 200
_alerts: deque[dict] = deque(maxlen=MAX_ALERTS)


def record_alert(alert_name: str, severity: str, status: str, summary: str, channels: list[str]) -> None:
    _alerts.appendleft({
        "received_at": datetime.now(timezone.utc).isoformat(),
        "alertname": alert_name,
        "severity": severity,
        "status": status,
        "summary": summary,
        "channels": channels,
    })


def get_alerts() -> list[dict]:
    return list(_alerts)