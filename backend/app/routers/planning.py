
from fastapi import APIRouter
from datetime import datetime
from ..models import OptimizationRequest
from ..services import forecast, service_time, optimizer

router = APIRouter()

@router.post("/optimize")
def optimize(req: OptimizationRequest):
    df = forecast.simple_forecast(datetime.utcnow(), req.horizon_hours)
    svc = service_time.estimate_service_time()
    shift_plan = optimizer.optimize_shift(df, svc)
    return {"plan": shift_plan}
