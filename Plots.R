library(ggplot2)
library(raster)
library(rasterVis)
library(viridis)
library(gridExtra)
library(cowplot)
setwd("C:/TFM/Modelados Maxent/P.halepensis/maps_reescalados_2")

# Obtener la lista de archivos TIFF
files <- list.files(path = "C:/TFM/Modelados Maxent/P.halepensis/maps_reescalados_2", pattern = "tif", full.names = TRUE, recursive = TRUE)

# Apilar los archivos TIFF en un objeto RasterStack
s <- stack(files)

# Crear la cuadrícula de gráficos
p <- levelplot(s, layout = c(3, 4), names.attr = c("2021-2040 ssp 245", "2021-2040 ssp 370", "2021-2040 ssp 585",
                                                   "2041-2060 ssp 245", "2041-2060 ssp 370", "2041-2060 ssp 585",
                                                   "2061-2080 ssp 245", "2061-2080 ssp 370", "2061-2080 ssp 585",
                                                   "2081-2100 ssp 245", "2081-2100 ssp 370", "2081-2100 ssp 585"),
               par.settings = rasterTheme(region = viridis(255)), margin = FALSE)

 # Crear el título general con el nombre de la especie en cursiva
title_general <- ggdraw() +
draw_label(expression(paste("Escenarios futuros para ", italic("Pinus halepensis_2"))), size = 20, hjust = 0.5)

# Ajustar el tamaño del gráfico y los títulos
p_combined <- plot_grid(title_general, p, ncol = 1, rel_heights = c(0.1, 0.9))

# Guardar la visualización como un archivo JPG
jpeg(file = "Future.jpg", width = 10000, height = 8000, res = 1000)
print(p_combined)
dev.off()

# Guardar la visualización como un archivo PNG
png(file = "Future.png", width = 10000, height = 8000, res = 1000)
print(p_combined)
dev.off()

##present time

setwd("C:/TFM/Modelados Maxent/P.halepensis/current_2")

raster=raster("C:/TFM/Modelados Maxent/P.halepensis/current_2/current.tif")

library(rgdal)
occs<-readOGR("C:/TFM/Modelados Maxent/P.halepensis/occurences/occurences.shp")

jpeg(file="present_time.jpg", width=10000, height=8000, res = 1000)

rasterVis::levelplot(raster,  par.settings=rasterTheme(viridis_pal(option = "H")(255)), main = "Ocurrencias actuales de Pinus halepensis", margin = FALSE) + 
  latticeExtra::layer(sp.points(occs, pch=19, cex=0.8, col="red"))

dev.off()

getwd()
