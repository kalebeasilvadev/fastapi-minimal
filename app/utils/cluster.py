import psutil

from app.utils.converters import bytes_to_mb


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