from pydantic import BaseModel
from datetime import datetime

class CPU(BaseModel):
    percent: float
    cores: int

class Memory(BaseModel):
    total: int
    used: int
    percent: float

class Disk(BaseModel):
    total: int
    used: int
    percent: float

class MetricsResponse(BaseModel):
    cpu: CPU
    memory: Memory
    disk: Disk

#///////////////////////////////////////////////////////////////////////

class MetricsHistoryResponse(BaseModel):
    cpu_percent : float
    disk_percent : float
    memory_percent : float
    created_at : datetime

    class Config:
        from_attributes = True
