from app.api.router import router
from app.core.status import get_status

from app.schemas.health import HealthSchema


@router.get("/health", response_model=HealthSchema)
async def read_health():
    return get_status()
