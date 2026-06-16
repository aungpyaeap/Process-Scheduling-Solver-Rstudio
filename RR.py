import numpy as np
import pandas as pd

ARRIVALS = np.array([0, 3, 4, 8, 12])
BURST = np.array([15, 2, 6, 2, 10])
Q = 2;

def round_robin(ARRIVALS, BURST, Q):
    n = len(ARRIVALS)
    
    remaining = BURST.copy()
    completion_time = np.zeros(n)
    start_time = np.full(n, -1)  # -1 means not started yet
    first_start = np.full(n, -1)  # To store the first start time
    
    current_time = 0
    queue = []
    completed = 0
    scheduling_table = []
    
    if ARRIVALS[0] == 0:
        queue.append(0)
    
    while completed < n:
        if not queue:
            next_arrival = float('inf')
            for i in range(n):
                if remaining[i] > 0 and ARRIVALS[i] < next_arrival:
                    next_arrival = ARRIVALS[i]
            if next_arrival == float('inf'):
                break
            current_time = next_arrival
            for i in range(n):
                if ARRIVALS[i] <= current_time and remaining[i] > 0 and i not in queue:
                    queue.append(i)
            continue
        
        pid = queue.pop(0)
        
        if first_start[pid] == -1:
            first_start[pid] = current_time
        
        execution_time = min(Q, remaining[pid])
        start = current_time
        end = current_time + execution_time
        remaining[pid] -= execution_time
        scheduling_table.append([f"P{pid+1}", start, end, execution_time, remaining[pid]])
    
        current_time = end
        for i in range(n):
            if ARRIVALS[i] > start and ARRIVALS[i] <= current_time and remaining[i] > 0 and i not in queue:
                queue.append(i)
        
        if remaining[pid] > 0:
            queue.append(pid)
        else:
            completion_time[pid] = current_time
            completed += 1
    
    turnaround_time = completion_time - ARRIVALS
    waiting_time = turnaround_time - BURST
    
    results_df = pd.DataFrame({
        'P': [f"P{i+1}" for i in range(n)],
        'AT': ARRIVALS,
        'BT': BURST,
        'ST': first_start.astype(int),
        'CT': completion_time.astype(int),
        'WT': waiting_time.astype(int),
        'TT': turnaround_time.astype(int)
    })
    
    scheduling_df = pd.DataFrame(scheduling_table, columns=['PROCESS', 'START', 'END', 'Q', 'LEFT'])
    
    print(f"\nRound Robin (RR) Scheduling\n")
    print(results_df.to_string(index=False))
    avg_waiting = np.mean(waiting_time)
    avg_turnaround = np.mean(turnaround_time)
    print(f"Average Waiting Time: {avg_waiting:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")
    print("\nScheduling Table:")
    print(scheduling_df.to_string(index=False))
    
    return scheduling_table, scheduling_df, avg_waiting, avg_turnaround

round_robin(ARRIVALS, BURST, Q)