from functools import lru_cache
from pathlib import Path
import yaml

ROUTING_CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "routing.yml"


@lru_cache
def _load_routing() -> dict:
    with open(ROUTING_CONFIG_PATH) as f:
        return yaml.safe_load(f)


def get_channels_for_severity(severity: str) -> list[str]:
    routing = _load_routing()
    return routing.get(severity, routing.get("default", []))