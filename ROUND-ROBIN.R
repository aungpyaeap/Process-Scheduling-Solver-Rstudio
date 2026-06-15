cat("\014")

arrivals <- c(0, 3, 4, 8, 12)
ext <- c(15, 2, 6, 2, 10)
Q <- 2

if (length(arrivals) == length(ext)) {
  cat("Number of Process:", length(arrivals), "\n")
  cat("Total Burst Time:", sum(ext), "\n")
  cat("Time Quantum:", Q, "\n\n")
  
  n <- length(arrivals)
  # Round Robin Scheduling Algorithm
  remaining_bt <- ext
  process_status <- data.frame(
    Process = paste0("P", 1:n),
    AT = arrivals,
    BT = ext,
    Remaining = ext,
    CT = numeric(n),
    WT = numeric(n),
    TT = numeric(n),
    Completed = logical(n)
  )
  
  current_time <- 0
  completed_count <- 0
  queue <- c()
  detail_table <- data.frame(
    PROCESS = character(),
    START = numeric(),
    END = numeric(),
    Q = numeric(),
    LEFT = numeric(),
    stringsAsFactors = FALSE
  )
  
  for (i in 1:n) {
    if (process_status$AT[i] <= current_time) {
      queue <- c(queue, i)
    }
  }
  
  while (completed_count < n) {
    if (length(queue) == 0) {
      next_arrival <- min(process_status$AT[!process_status$Completed])
      current_time <- next_arrival
      for (i in 1:n) {
        if (process_status$AT[i] <= current_time && 
            !process_status$Completed[i] && 
            !(i %in% queue)) {
          queue <- c(queue, i)
        }
      }
      next
    }
    
    current_process <- queue[1]
    queue <- queue[-1]
    start_time <- current_time
    exec_time <- min(Q, process_status$Remaining[current_process])
    current_time <- current_time + exec_time
    process_status$Remaining[current_process] <- process_status$Remaining[current_process] - exec_time
    detail_table <- rbind(detail_table, data.frame(
      PROCESS = process_status$Process[current_process],
      START = start_time,
      END = current_time,
      Q = exec_time,
      LEFT = process_status$Remaining[current_process]
    ))
    
    for (i in 1:n) {
      if (process_status$AT[i] > start_time && 
          process_status$AT[i] <= current_time && 
          !process_status$Completed[i] && 
          !(i %in% queue)) {
        queue <- c(queue, i)
      }
    }
    
    if (process_status$Remaining[current_process] > 0) {
      queue <- c(queue, current_process)
    } else {
      process_status$Completed[current_process] <- TRUE
      process_status$CT[current_process] <- current_time
      process_status$TT[current_process] <- process_status$CT[current_process] - process_status$AT[current_process]
      process_status$WT[current_process] <- process_status$TT[current_process] - process_status$BT[current_process]
      completed_count <- completed_count + 1
    }
  }
  
  cat("Round Robin Scheduling Results:\n")
  cat("Process\tAT\tBT\tCT\tWT\tTT\n")
  for (i in 1:n) {
    cat(sprintf("%s\t%d\t%d\t%d\t%d\t%d\n", 
                process_status$Process[i], 
                process_status$AT[i], 
                process_status$BT[i], 
                process_status$CT[i], 
                process_status$WT[i], 
                process_status$TT[i]))
  }
  cat("Average WT:", mean(process_status$WT), "\n")
  cat("Average TT:", mean(process_status$TT), "\n\n")
  
  cat("Detailed Round Robin Execution Table:\n")
  cat("PROCESS\tSTART\tEND\tQ\tLEFT\n")
  for (i in 1:nrow(detail_table)) {
    cat(sprintf("%s\t%d\t%d\t%d\t%d\n", 
                detail_table$PROCESS[i],
                detail_table$START[i],
                detail_table$END[i],
                detail_table$Q[i],
                detail_table$LEFT[i]))
  }
  
} else {
  stop("Arrays have different lengths.")
}