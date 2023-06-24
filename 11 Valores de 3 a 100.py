import os
import arcpy
from arcpy.sa import *

# Establecer el entorno de trabajo
arcpy.env.workspace = r"C:\TFM\Modelados Maxent\Q.rotundifolia\Inputs_Guidos\0a100"

# Obtener la lista de rasters en el directorio
raster_list = arcpy.ListRasters()

# Ruta de salida para los nuevos rasters
output_folder = r"C:\TFM\Modelados Maxent\Q.rotundifolia\Inputs_Guidos\Resistencias\3a100"

# Verificar si la carpeta de salida existe, si no, crearla
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Recorrer la lista de rasters y generar los nuevos rasters
for raster_name in raster_list:
    raster_path = arcpy.env.workspace + "\\" + raster_name

    # Crear objeto Raster a partir del archivo
    raster = arcpy.Raster(raster_path)

    # Ajustar los valores del raster para que estén comprendidos entre 3 y 100
    output_raster = Con(raster < 3, 3, Con(raster > 100, 100, raster))

    # Guardar el nuevo raster en la carpeta de salida
    output_path = output_folder + "\\" + raster_name
    output_raster.save(output_path)

    print("Nuevo raster generado: " + raster_name)

print("Proceso completado.")
