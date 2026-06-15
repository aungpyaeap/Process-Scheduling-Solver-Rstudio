cat("\014")

arrivals <- c(0, 3, 4, 8, 12)
ext <- c(15, 2, 6, 2, 10)

if (length(arrivals) == length(ext)) {
  cat("Arrivals:", length(arrivals), "\n")
  cat("Execution times:", length(ext), "\n")
  
  n <- length(arrivals)
  process <- data.frame(
    Process = paste0("P", 1:n),
    AT = arrivals,
    BT = ext,
    ST = numeric(n),
    CT = numeric(n),
    WT = numeric(n),
    TT = numeric(n)
  )
  
  current_time <- 0
  for (i in 1:n) {
    process$ST[i] <- max(current_time, process$AT[i])
    process$CT[i] <- process$ST[i] + process$BT[i]
    process$TT[i] <- process$CT[i] - process$AT[i]
    process$WT[i] <- process$TT[i] - process$BT[i]
    current_time <- process$CT[i]
  }
  
  cat("\n")
  cat("FCFS\tP\tAT\tBT\tST\tCT\tWT\tTT\n")
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
  cat("Average WT:", mean(process$TT), "\n")
} else {
  stop("Arrays have different lengths.")
}