
import pandas as pd
import joblib
from pathlib import Path
from datetime import datetime, timedelta

_MODEL_PATH = Path(__file__).parent.parent / "models" / "forecast.pkl"

def _load_model():
    if _MODEL_PATH.exists():
        return joblib.load(_MODEL_PATH)
    return None

_model = _load_model()

def simple_forecast(now: datetime, hours: int = 24):
    return pd.DataFrame({
        "timestamp": [now + timedelta(hours=h) for h in range(hours)],
        "pax": [150]*hours
    })

def forecast(now: datetime, hours: int = 24):
    if _model is None:
        return simple_forecast(now, hours)
    future = pd.date_range(now, periods=hours, freq='h')
    preds = _model.predict(future.to_frame(index=False))
    return pd.DataFrame({"timestamp": future, "pax": preds})
