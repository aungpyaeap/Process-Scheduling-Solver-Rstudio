import numpy as np
import pandas as pd

ARRIVALS = np.array([0, 3, 4, 8, 12])
BURST = np.array([15, 2, 6, 2, 10])

def fcfs(ARRIVALS, BURST):
    n = len(ARRIVALS)
    ST = np.zeros(n, dtype=int)  # Initialize Start Time
    CT = np.zeros(n, dtype=int)  # Initialize Completion Time
    WT = np.zeros(n, dtype=int)  # Initialize Waiting Time
    TT = np.zeros(n, dtype=int)  # Initialize Turnaround Time
    
    current_time = 0
    
    for i in range(n):
        ST[i] = max(current_time, ARRIVALS[i])
        CT[i] = ST[i] + BURST[i]
        WT[i] = ST[i] - ARRIVALS[i]
        TT[i] = CT[i] - ARRIVALS[i]
        current_time = CT[i]
    
    df = pd.DataFrame({
        'Process': [f'P{i+1}' for i in range(n)],
        'AT': ARRIVALS,
        'BT': BURST,
        'ST': ST,
        'CT': CT,
        'WT': WT,
        'TT': TT
    })
    
    avg_waiting = np.mean(WT)
    avg_turnaround = np.mean(TT)
    
    print(f"\nFirst Come First Serve (FCFS) Scheduling\n")
    print(df.to_string(index=False))
    print(f"Average Waiting Time: {avg_waiting:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")
    
    return df, avg_waiting, avg_turnaround

fcfs(ARRIVALS, BURST)