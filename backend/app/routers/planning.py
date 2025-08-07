
from fastapi import APIRouter
from datetime import datetime
import pandas as pd
from ..services import forecast as fc, optimizer, service_time
from ..schemas import OptimizationRequest

router = APIRouter()

@router.post("/optimize")
def optimize(req: OptimizationRequest):
    if req.demand:
        df = pd.DataFrame([d.dict() for d in req.demand])
    else:
        df = fc.forecast(datetime.utcnow(), req.horizon_hours)
    svc = service_time.estimate_service_time()
    plan = optimizer.build_plan(df, svc)
    return {"plan": plan}
