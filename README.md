# Process Scheduling Solver (Rstudio)

R codes for classic CPU scheduling algorithms to compute Turnaround Time (TT) and Waiting Time (WT).

## Algorithms in repository
- First Come First Serve / FCFS
- Shortest Job First / SJF (non-preemptive)
- Preemptive Priority
- Round-Robin / RR

## Equations
$\text{Start Time with different arrival time}=\max\{\underbrace{ST + EXT}_{\text{previous}(i-1)} , \underbrace{AT}_{\text{current}(i)}\}$

$\text{Completion Time}=\text{Start Time}+\text{Execution Time}$

$\text{Waiting Time}=\text{Start Time}+\text{Arrival Time}$

$\text{Turnaround Time}=\text{Completion Time}+\text{Arrival Time}$

$\text{Remaining Execution Time}= \text{Execution Time}(a) – (\text{Start Time}(b) – \text{Start Time}(a))$

Note that counting starts from remaining blocks.

Use
$\text{Waiting Time} = (\text{Completion Time} – \text{Arrival Time}) – \text{Execution Time}$

for a process with prevented blocks. Applicable for Preemptive Priority and Round-Robin.

$\text{Average Waiting Time} \quad WT = \frac{1}{n} \sum_{i=1}^n WT_i, \quad i=1,2,\cdots,n$

$\text{Average Turnaround Time} \quad TT = \frac{1}{n} \sum_{i=1}^n TT_i, \quad i=1,2,\cdots,n$


