cat("\014")

arrivals <- c(0, 3, 4, 8, 12)
ext <- c(15, 2, 6, 2, 10)
priority <- c(5, 1, 3, 4, 2)

if (length(arrivals) == length(ext) && length(arrivals) == length(priority)) {
  cat("Number of Process:", length(arrivals), "\n")
  cat("Total Burst Time:", sum(ext), "\n")
  
  n <- length(arrivals)
  process <- data.frame(
    Process = paste0("P", 1:n),
    AT = arrivals,
    BT = ext,
    Priority = priority,
    ST = numeric(n),
    CT = numeric(n),
    WT = numeric(n),
    TT = numeric(n),
    Remaining = ext,  # Remaining burst time
    Completed = logical(n)
  )
  
  # Preemptive Priority Scheduling Algorithm
  # Select process with highest priority (lowest priority number)
  current_time <- 0
  completed_count <- 0
  last_selected <- NULL
  start_time_recorded <- rep(FALSE, n)
  while (completed_count < n) {
    available <- which(process$AT <= current_time & !process$Completed)
    if (length(available) > 0) {
      selected <- available[which.min(process$Priority[available])]
      if (length(selected) > 1) {
        selected <- selected[which.min(process$AT[selected])]
      }
      
      if (!start_time_recorded[selected]) {
        process$ST[selected] <- current_time
        start_time_recorded[selected] <- TRUE
      }
      
      next_arrival_time <- min(process$AT[!process$Completed & process$AT > current_time], Inf)
      if (next_arrival_time == Inf) {
        exec_time <- process$Remaining[selected]
      } else {
        exec_time <- min(process$Remaining[selected], next_arrival_time - current_time)
      }
      process$Remaining[selected] <- process$Remaining[selected] - exec_time
      current_time <- current_time + exec_time
      
      if (process$Remaining[selected] == 0) {
        process$CT[selected] <- current_time
        process$TT[selected] <- process$CT[selected] - process$AT[selected]
        process$WT[selected] <- process$TT[selected] - process$BT[selected]
        process$Completed[selected] <- TRUE
        completed_count <- completed_count + 1
      }
    } else {
      current_time <- min(process$AT[!process$Completed])
    }
  }
  
  cat("\n")
  cat("Preemptive Priority\tP\tAT\tBT\tPriority\tST\tCT\tWT\tTT\n")
  for (i in 1:n) {
    cat(sprintf("\t\t\t%s\t%d\t%d\t%d\t\t%d\t%d\t%d\t%d\n", 
                process$Process[i], 
                process$AT[i], 
                process$BT[i],
                process$Priority[i],
                process$ST[i], 
                process$CT[i], 
                process$WT[i], 
                process$TT[i]))
  }
  cat("\nAverage WT:", mean(process$WT), "\n")
  cat("Average TT:", mean(process$TT), "\n")
} else {
  stop("Arrays have different lengths.")
}