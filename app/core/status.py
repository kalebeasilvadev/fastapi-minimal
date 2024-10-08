import psutil

from app.utils.converters import bytes_to_mb
from app.schemas.health import HealthSchema


def get_cpu():
    return psutil.cpu_percent(interval=1)


def get_memory():
    memory = psutil.virtual_memory()
    return {
        "total": bytes_to_mb(memory.total),
        "free": bytes_to_mb(memory.free),
        "used": bytes_to_mb(memory.used),
        "percent": memory.percent,
    }


def get_disk():
    disk = psutil.disk_usage('/')
    return {
        "total": bytes_to_mb(disk.total),
        "free": bytes_to_mb(disk.free),
        "used": bytes_to_mb(disk.used),
        "percent": disk.percent,
    }


def get_status() -> HealthSchema:
    cluster = {
        "cpu_percent": get_cpu(),
        "memory": get_memory(),
        "disk": get_disk(),
    }
    status = "OK"
    description = "Everything is running smoothly"

    if cluster["cpu_percent"] > 90:
        status = "WARNING"
        description = "High CPU usage"
    if cluster["memory"]["percent"] > 90:
        status = "WARNING"
        description = "High memory usage"
    if cluster["disk"]["percent"] > 90:
        status = "WARNING"
        description = "High disk usage"
    if cluster["cpu_percent"] > 90 and cluster["memory"]["percent"] > 90 and cluster["disk"]["percent"] > 90:
        status = "CRITICAL"
        description = "High CPU, memory and disk usage"

    return HealthSchema(status=status, description=description, cluster=cluster)
