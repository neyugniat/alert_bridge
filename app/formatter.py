from app.models import Alert

STATUS_ICONS = {
    "firing": "🔥",
    "resolved": "✅",
}

SEVERITY_ICONS = {
    "critical": "🔴",
    "warning": "🟠",
    "info": "🔵",
}


def format_alert(alert: Alert) -> str:
    name = alert.labels.get("alertname", "UnknownAlert")
    severity = alert.labels.get("severity", "unknown")
    status = alert.status

    status_icon = STATUS_ICONS.get(status, "❔")
    severity_icon = SEVERITY_ICONS.get(severity, "⚪")

    summary = alert.annotations.get("summary") or alert.annotations.get("description", "no summary provided")

    extra_labels = {
        k: v for k, v in alert.labels.items()
        if k not in ("alertname", "severity")
    }
    labels_str = ", ".join(f"{k}={v}" for k, v in extra_labels.items()) or "none"

    lines = [
        f"{status_icon} [{status.upper()}] {name} {severity_icon} {severity}",
        f"{summary}",
        f"Labels: {labels_str}",
        f"Started: {alert.startsAt.strftime('%Y-%m-%d %H:%M:%S UTC')}",
    ]

    if status == "resolved":
        lines.append(f"Resolved: {alert.endsAt.strftime('%Y-%m-%d %H:%M:%S UTC')}")

    if alert.generatorURL:
        lines.append(f"Source: {alert.generatorURL}")

    return "\n".join(lines)