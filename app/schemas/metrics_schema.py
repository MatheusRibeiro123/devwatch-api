from pydantic import BaseModel

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