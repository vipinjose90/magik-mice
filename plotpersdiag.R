require("TDA")
pdf("persdiag.pdf")
data <- read.table("points.dgm", sep = " ", quote="\"", comment.char="")
inData = as.matrix(data)
maxval = max(inData[inData != Inf])
for(i in 1:nrow(inData)){
  if(is.infinite(inData[i,3])){
    inData[i,3] = maxval + 1.5
  }
}
plot.diagram(inData, diagLim = NULL, dimension = NULL, col = NULL, rotated = FALSE,
     barcode = FALSE, band = NULL, lab.line = 2.2, colorBand = "pink",
     colorBorder = NA, add = FALSE)
dev.off()