
import pandas as pd
from datetime import datetime, timedelta

def simple_forecast(now: datetime, hours: int = 24):
    # Dummy constant forecast
    future = []
    for h in range(hours):
        ts = now + timedelta(hours=h)
        future.append({"timestamp": ts.isoformat(), "pax": 100 + (h % 6)*20})
    return pd.DataFrame(future)
