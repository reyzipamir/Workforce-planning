from pydantic import BaseModel
from typing import List
from datetime import datetime


class DemandPoint(BaseModel):
    timestamp: datetime
    pax: int


class OptimizationRequest(BaseModel):
    horizon_hours: int
    demand: List[DemandPoint] | None = None
