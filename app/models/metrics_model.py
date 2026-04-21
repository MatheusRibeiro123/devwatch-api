from sqlalchemy import Column,Integer,Float,DateTime
from datetime import datetime
from app.database import Base

class Metrics(Base):
    __tablename__ = "metrics"
    
    id = Column(Integer,primary_key=True,index = True)
    cpu_percent = Column(Float)
    disk_percent = Column(Float)
    memory_percent = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
