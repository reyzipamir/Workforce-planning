
from ortools.linear_solver import pywraplp
import pandas as pd
from datetime import datetime

def optimize_shift(demand_df: pd.DataFrame, service_seconds: int, max_shift_len=8):
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        raise RuntimeError("SCIP not available")

    hours = list(range(len(demand_df)))
    x = {h: solver.IntVar(0, solver.infinity(), f'x_{h}') for h in hours}

    for h, row in demand_df.iterrows():
        need = int((row['pax'] * service_seconds) / 3600)  # simplistic
        solver.Add(x[h] >= need)

    solver.Minimize(solver.Sum(x[h] for h in hours))
    result = solver.Solve()

    plan = []
    if result == pywraplp.Solver.OPTIMAL:
        for h in hours:
            ts = demand_df.iloc[h]['timestamp']
            plan.append({"timestamp": ts, "headcount": int(x[h].solution_value())})
    return plan
