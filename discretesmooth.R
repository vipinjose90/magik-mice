require("itsmr")

args <- commandArgs(trailingOnly = TRUE)
notsmooth <- (read.csv(args[1],header=F))[,1]

y <- smooth.fft(notsmooth, as.numeric(args[2]))
write.table(y, file = "lowpass-mice-full.csv",row.names = FALSE,col.names = FALSE)
y <- y[seq(from = 1, to = length(y), by = 100)]
write.table(y, file = "smoothed-mice-norank.csv",row.names = FALSE,col.names = FALSE)
y <- smooth.rank(y,2)
write.table(y, file = "smoothed-mice.csv",row.names = FALSE,col.names = FALSE)

print("Input smoothed!")

