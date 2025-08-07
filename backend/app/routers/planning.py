from fastapi import APIRouter
from datetime import datetime
import pandas as pd

from ..services import forecast, optimizer, service_time
from ..schemas import OptimizationRequest

router = APIRouter()

@router.post("/optimize")
def optimize(req: OptimizationRequest):
    # 1) build demand DataFrame
    if req.demand:
        df = pd.DataFrame([d.dict() for d in req.demand])
    else:
        df = forecast.simple_forecast(datetime.utcnow(), req.horizon_hours)

    svc = service_time.estimate_service_time()
    plan = optimizer.build_plan(df, svc)
    return {"plan": plan}
