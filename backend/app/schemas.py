
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class DemandPoint(BaseModel):
    timestamp: datetime
    pax: int

class OptimizationRequest(BaseModel):
    horizon_hours: int = 24
    demand: Optional[List[DemandPoint]] = None
