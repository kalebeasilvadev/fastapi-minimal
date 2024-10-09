from app.schemas.health import HealthSchema
from app.utils.cluster import get_cpu, get_disk, get_memory


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
