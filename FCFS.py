import numpy as np
from tabulate import tabulate

ARRIVALS = np.array([0, 3, 4, 8, 12])
BURST = np.array([15, 2, 6, 2, 10])

# Number of processes
n = len(ARRIVALS)

# Sort processes by arrival time
process_indices = np.argsort(ARRIVALS)
sorted_arrivals = ARRIVALS[process_indices]
sorted_burst = BURST[process_indices]
sorted_processes = [f'P{i+1}' for i in process_indices]

# Initialize arrays for results
START_TIME = np.zeros(n, dtype=int)
COMPLETION_TIME = np.zeros(n, dtype=int)
WAITING_TIME = np.zeros(n, dtype=int)
TURNAROUND_TIME = np.zeros(n, dtype=int)

# Calculate FCFS scheduling
current_time = 0

for i in range(n):
    # Start time is max of current time and arrival time
    START_TIME[i] = max(current_time, sorted_arrivals[i])
    
    # Completion time = start time + burst time
    COMPLETION_TIME[i] = START_TIME[i] + sorted_burst[i]
    
    # Turnaround time = completion time - arrival time
    TURNAROUND_TIME[i] = COMPLETION_TIME[i] - sorted_arrivals[i]
    
    # Waiting time = turnaround time - burst time
    WAITING_TIME[i] = TURNAROUND_TIME[i] - sorted_burst[i]
    
    # Update current time to completion time
    current_time = COMPLETION_TIME[i]

# Prepare results table
RESULTS = []
for i in range(n):
    RESULTS.append([
        sorted_processes[i],
        sorted_arrivals[i],
        sorted_burst[i],
        START_TIME[i],
        COMPLETION_TIME[i],
        WAITING_TIME[i],
        TURNAROUND_TIME[i]
    ])

# Print the table
headers = ['P', 'AT', 'BT', 'ST', 'CT', 'WT', 'TT']
print(tabulate(RESULTS, headers=headers, tablefmt='grid'))

# Calculate and print averages
avg_waiting = np.mean(WAITING_TIME)
avg_turnaround = np.mean(TURNAROUND_TIME)

print(f"\nAverage Waiting Time: {avg_waiting:.2f}")
print(f"Average Turnaround Time: {avg_turnaround:.2f}")