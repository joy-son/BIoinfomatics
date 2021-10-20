#! /usr/bin/env Rscript

data <- read.table("figure.tsv", header = TRUE, sep = "\t")
f_data <- data[data$Count>1,]
label <- paste(f_data[[1]],' ',f_data[[4]],"%")
index <- paste(data[[1]],':',data[[2]])
png(filename = "figure.png", width=1600, height=800)
pie(f_data[[3]], labels=label, main= "Cluster of Orthologus Groups (COG)", clockwise=TRUE)
Rasterize[Plot[...]]
legend(1.1,0.6,index, fill=NULL)
dev.off()
