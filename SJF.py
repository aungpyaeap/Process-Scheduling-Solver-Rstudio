import numpy as np
import pandas as pd

ARRIVALS = np.array([0, 3, 4, 8, 12])
BURST = np.array([15, 2, 6, 2, 10])

def sjf(ARRIVALS, BURST):
    n = len(ARRIVALS)
    ST = np.zeros(n, dtype=int)  # Initialize Start Time
    CT = np.zeros(n, dtype=int)  # Initialize Completion Time
    WT = np.zeros(n, dtype=int)  # Initialize Waiting Time
    TT = np.zeros(n, dtype=int)  # Initialize Turnaround Time
    completed = np.zeros(n, dtype=bool)  # Track completed processes
    remaining_burst = BURST.copy()
    
    current_time = 0
    completed_count = 0
    
    while completed_count < n:
        shortest_job = -1
        shortest_burst = float('inf')
        
        for i in range(n):
            if not completed[i] and ARRIVALS[i] <= current_time:
                if remaining_burst[i] < shortest_burst:
                    shortest_burst = remaining_burst[i]
                    shortest_job = i
        
        if shortest_job == -1:
            next_arrival = min(ARRIVALS[i] for i in range(n) if not completed[i])
            current_time = next_arrival
            continue
        
        ST[shortest_job] = current_time
        CT[shortest_job] = current_time + BURST[shortest_job]
        WT[shortest_job] = ST[shortest_job] - ARRIVALS[shortest_job]
        TT[shortest_job] = CT[shortest_job] - ARRIVALS[shortest_job]
        
        current_time = CT[shortest_job]
        completed[shortest_job] = True
        completed_count += 1
    
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
    
    print(f"\nShortest Job First (SJF) Scheduling - Non-Preemptive\n")
    print(df.to_string(index=False))
    print(f"Average Waiting Time: {avg_waiting:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")
    
    return df, avg_waiting, avg_turnaround

sjf(ARRIVALS, BURST)