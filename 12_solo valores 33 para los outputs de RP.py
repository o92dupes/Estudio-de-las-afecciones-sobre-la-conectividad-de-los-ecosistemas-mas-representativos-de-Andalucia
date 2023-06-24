import arcpy
from arcpy.sa import *
import os

# Directorio de entrada y salida
input_directory = r"G:\TFM\Resultados Restoration planner\P.pinaster\Pathways"
output_directory = r"G:\TFM\Resultados Restoration planner\P.pinaster\Pathways\only33"

# Obtener la lista de archivos raster en el directorio de entrada
arcpy.env.workspace = input_directory
raster_list = arcpy.ListRasters("*", "TIF")

# Crear la carpeta de salida si no existe
if not arcpy.Exists(output_directory):
    arcpy.CreateFolder_management(os.path.dirname(output_directory), os.path.basename(output_directory))

# Configurar el entorno de procesamiento
arcpy.env.overwriteOutput = True

# Recorrer los archivos raster en el directorio de entrada
for raster_file in raster_list:
    # Ruta completa del archivo de entrada
    input_raster = os.path.join(input_directory, raster_file)

    # Ruta de salida del nuevo archivo raster
    output_raster = os.path.join(output_directory, raster_file)

    # Cargar el raster
    raster = arcpy.Raster(input_raster)

    # Aplicar la condición de igualdad para seleccionar los valores 33 y establecer el resto en NoData
    selected_raster = Con(raster == 33, raster, SetNull(raster, raster, "VALUE <> 33"))

    # Guardar el nuevo archivo raster
    selected_raster.save(output_raster)

    print("Archivo procesado: {0}".format(raster_file))

print("Proceso completado")
