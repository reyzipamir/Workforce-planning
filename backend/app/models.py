
from pydantic import BaseModel
from typing import List, Dict

class DemandPoint(BaseModel):
    timestamp: str
    pax: int

class ShiftPlan(BaseModel):
    start: str
    end: str
    headcount: int

class OptimizationRequest(BaseModel):
    horizon_hours: int = 24
    demand: List[DemandPoint]
