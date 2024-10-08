from typing import Optional

from pydantic import BaseModel


class MemoryHealthSchema(BaseModel):
    total: Optional[float] = 0
    free: Optional[float] = 0
    used: Optional[float] = 0
    percent: Optional[float] = 0


class DiskHealthSchema(BaseModel):
    total: Optional[float] = 0
    free: Optional[float] = 0
    used: Optional[float] = 0
    percent: Optional[float] = 0


class ClusterHealthSchema(BaseModel):
    cpu_percent: Optional[float] = 0
    memory: MemoryHealthSchema
    disk: DiskHealthSchema


class HealthSchema(BaseModel):
    status: str
    description: str
    cluster: ClusterHealthSchema
