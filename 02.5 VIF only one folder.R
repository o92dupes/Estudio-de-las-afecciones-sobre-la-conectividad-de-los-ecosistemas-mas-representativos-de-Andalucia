library(usdm)
setwd("C:/TFM/Worldclimedata_def/Historical_clipped_halepensis")

# Get list of files and create stack
myExpl <- list.files(pattern = ".tif")
myExpl <- stack(myExpl)

# Calculate VIF and exclude layers with high correlation and variance inflation factor
v <- vif(myExpl)
v2 <- vifcor(myExpl, th = 0.75)
myExpl <- exclude(myExpl, v2)
v1 <- vifstep(myExpl, th = 10)
myExpl <- exclude(myExpl, v1)

# Write names of remaining layers to text file
remaining_layers <- names(myExpl)
write.table(remaining_layers, file = "remaining_layers.txt", quote = FALSE, col.names = FALSE, row.names = FALSE)

# Print remaining layers
print(myExpl)

