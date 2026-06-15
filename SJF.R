cat("\014")

arrivals <- c(0, 3, 4, 8, 12)
ext <- c(15, 2, 6, 2, 10)

if (length(arrivals) == length(ext)) {
  cat("Number of Process:", length(arrivals), "\n")
  cat("Total Burst Time:", sum(ext), "\n")
  
  n <- length(arrivals)
  process <- data.frame(
    Process = paste0("P", 1:n),
    AT = arrivals,
    BT = ext,
    ST = numeric(n),
    CT = numeric(n),
    WT = numeric(n),
    TT = numeric(n),
    Completed = logical(n)
  )
  
  # SJF (Non-preemptive) Scheduling Algorithm
  current_time <- 0
  completed_count <- 0
  
  while (completed_count < n) {
    available <- which(process$AT <= current_time & !process$Completed)
    
    if (length(available) > 0) {
      selected <- available[which.min(process$BT[available])]
      if (length(selected) > 1) {
        selected <- selected[which.min(process$AT[selected])]
      }
      
      process$ST[selected] <- current_time
      process$CT[selected] <- current_time + process$BT[selected]
      process$TT[selected] <- process$CT[selected] - process$AT[selected]
      process$WT[selected] <- process$TT[selected] - process$BT[selected]
      process$Completed[selected] <- TRUE
      current_time <- process$CT[selected]
      completed_count <- completed_count + 1
    } else {
      next_arrival <- min(process$AT[!process$Completed])
      current_time <- next_arrival
    }
  }
  
  cat("\n")
  cat("SJF\tP\tAT\tBT\tST\tCT\tWT\tTT\n")
  for (i in 1:n) {
    cat(sprintf("\t%s\t%d\t%d\t%d\t%d\t%d\t%d\n", 
                process$Process[i], 
                process$AT[i], 
                process$BT[i], 
                process$ST[i], 
                process$CT[i], 
                process$WT[i], 
                process$TT[i]))
  }
  cat("Average WT:", mean(process$WT), "\n")
  cat("Average TT:", mean(process$TT), "\n")
} else {
  stop("Arrays have different lengths.")
}