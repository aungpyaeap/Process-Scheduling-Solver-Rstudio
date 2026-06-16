import numpy as np
import pandas as pd

ARRIVALS = np.array([0, 3, 4, 8, 12])
BURST = np.array([15, 2, 6, 2, 10])
PRIORITY= np.array([5, 1, 3, 4, 2])

def preemptive_priority(ARRIVALS, BURST, PRIORITY):
    n = len(ARRIVALS)
    
    processes = []
    for i in range(n):
        processes.append({
            'pid': 'P' + str(i+1),
            'arrival': ARRIVALS[i],
            'burst': BURST[i],
            'priority': PRIORITY[i],
            'remaining': BURST[i],
            'start_time': None,
            'completion_time': 0,
            'waiting_time': 0,
            'turnaround_time': 0
        })
    
    current_time = 0
    completed = 0
    last_process = -1
    
    while completed < n:
        selected = -1
        highest_priority = float('inf')
        
        for i in range(n):
            if (processes[i]['remaining'] > 0 and 
                processes[i]['arrival'] <= current_time):
                if processes[i]['priority'] < highest_priority:
                    highest_priority = processes[i]['priority']
                    selected = i
        
        if selected == -1:
            current_time += 1
            continue
        
        if processes[selected]['start_time'] is None:
            processes[selected]['start_time'] = current_time
        
        processes[selected]['remaining'] -= 1
        current_time += 1
        
        if processes[selected]['remaining'] == 0:
            processes[selected]['completion_time'] = current_time
            processes[selected]['turnaround_time'] = (current_time - processes[selected]['arrival'])
            processes[selected]['waiting_time'] = (processes[selected]['turnaround_time'] - processes[selected]['burst'])
            completed += 1
    
    df = pd.DataFrame(processes)
    df = df[['pid', 'arrival', 'burst', 'priority', 'start_time', 
             'completion_time', 'waiting_time', 'turnaround_time']]
    df.columns = ['P', 'AT', 'BT', 'P*', 'ST', 'CT', 'WT', 'TT']
    
    avg_wt = df['WT'].mean()
    avg_tt = df['TT'].mean()
    
    print(f"\nPreemptive Priority (PP) Scheduling Results\n")
    print(df.to_string(index=False))
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tt:.2f}")
    
    return df, avg_wt, avg_tt

result_df = preemptive_priority(ARRIVALS, BURST, PRIORITY)