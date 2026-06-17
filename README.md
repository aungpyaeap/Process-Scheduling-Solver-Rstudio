# Process Scheduling Solver

![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=for-the-badge)

Pyton code for classic CPU scheduling algorithms to compute Average Waiting Time (WT) and Average Turnaround Time (TT).

## Algorithms in repository
- **`FCFS.py`**: First Come First Serve / FCFS
- **`SJF.py`**: Shortest Job First / SJF (non-preemptive)
- **`PP.py`**: Preemptive Priority
- **`RR.py`**: Round-Robin / RR

The implementations require the following packages:
- `numpy` - for numerical operations
- `tabulate` - for formatted table output

Install them using pip:
```pip install numpy tabulate```

## Equations
**Start Time with different arrival time:**

Start Time = max(previous Start Time + previous Execution Time, current Arrival Time)

---

**Completion Time:**

Completion Time = Start Time + Execution Time

---

**Waiting Time (basic):**

Waiting Time = Start Time - Arrival Time

---

**Turnaround Time:**

Turnaround Time = Completion Time - Arrival Time

---

**Remaining Execution Time:**

Remaining Execution Time = Execution Time(a) - (Start Time(b) - Start Time(a))

Note: Counting starts from remaining blocks.

---

**Waiting Time (for preemptive algorithms):**

Waiting Time = (Completion Time - Arrival Time) - Execution Time

Applies to: Preemptive Priority and Round-Robin

---

**Average Waiting Time:**

Average WT = (1/n) × (WT₁ + WT₂ + ... + WTₙ)

---

**Average Turnaround Time:**

Average TT = (1/n) × (TT₁ + TT₂ + ... + TTₙ)

![Visualisation of process scheduling](scheduling.png "Visualisation of process scheduling")