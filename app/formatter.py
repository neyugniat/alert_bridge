from app.models import Alert


def format_alert(alert: Alert) -> str:
    name = alert.labels.get("alertname", "UnknownAlert")
    severity = alert.labels.get("severity", "unknown")
    summary = alert.annotations.get("summary") or alert.annotations.get("description", "")

    return f"[{alert.status.upper()}] {name} (severity: {severity})\n{summary}"