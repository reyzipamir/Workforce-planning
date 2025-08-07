
import joblib
from pathlib import Path
import pandas as pd

_MODEL_PATH = Path(__file__).parent.parent / "models" / "service_time.pkl"
_model = joblib.load(_MODEL_PATH) if _MODEL_PATH.exists() else None

def estimate_service_time(features: dict | None = None):
    if _model is None or features is None:
        return 18  # default seconds
    df = pd.DataFrame([features])
    return float(_model.predict(df)[0])
