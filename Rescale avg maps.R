library(raster)
library(rgdal)

# Directorio de entrada (carpeta que contiene los archivos de mapa generados por MaxEnt)
directorio_entrada <- "C:/TFM/Modelados Maxent/P.halepensis/maps_2/"

# Directorio de salida (carpeta donde se guardarán los archivos reescalados)
directorio_salida <- "C:/TFM/Modelados Maxent/P.halepensis/maps_reescalados_2/"

# Obtener la lista de archivos en el directorio de entrada
archivos <- list.files(path = directorio_entrada, pattern = ".tif$", full.names = TRUE)

# Iterar sobre cada archivo
for (archivo in archivos) {
  # Cargar el archivo de mapa en formato TIFF
  mapa <- raster(archivo)
  
  # Calcular los valores mínimo y máximo del mapa
  min_val <- min(mapa[], na.rm = TRUE)
  max_val <- max(mapa[], na.rm = TRUE)
  
  # Reescalar los valores del mapa de 0 a 1
  mapa_reescalado <- (mapa - min_val) / (max_val - min_val)
  
  # Establecer explícitamente los valores mínimo y máximo del mapa reescalado
  setMinMax(mapa_reescalado, newmin = 0, newmax = 1)
  
  # Crear el nombre de archivo de salida
  archivo_salida <- paste0(directorio_salida, basename(archivo))
  
  # Guardar el mapa reescalado en el directorio de salida
  writeRaster(mapa_reescalado, filename = archivo_salida, format = "GTiff", overwrite=TRUE)
  
  cat("Archivo reescalado y guardado:", archivo_salida, "\n")
}

