
from ortools.sat.python import cp_model
import pandas as pd

def build_plan(demand_df: pd.DataFrame, service_seconds: int, shift_len=8):
    hours = range(len(demand_df))
    model = cp_model.CpModel()
    hvar = {h: model.NewIntVar(0, 200, f'h{h}') for h in hours}
    for h, row in demand_df.iterrows():
        need = int((row['pax'] * service_seconds + 3599)//3600)
        model.Add(hvar[h] >= need)
    model.Minimize(sum(hvar.values()))
    solver = cp_model.CpSolver()
    solver.Solve(model)
    return [{"timestamp": demand_df.iloc[h]['timestamp'].isoformat(),
             "headcount": int(solver.Value(hvar[h]))} for h in hours]
