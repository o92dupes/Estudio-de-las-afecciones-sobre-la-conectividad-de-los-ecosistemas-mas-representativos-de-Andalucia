import os
import arcpy
import shutil

# Crear el directorio de salida para los archivos TIFF
tiff_dir = r'C:\TFM\Modelados Maxent\Q.rotundifolia\maps_reescalados'
if not os.path.exists(tiff_dir):
    os.makedirs(tiff_dir)

# Definir la proyección de los archivos TIFF y guardarlos en el directorio para TIFF proyectados
sr = arcpy.SpatialReference('GCS_WGS_1984')

for file in os.listdir(tiff_dir):
    if file.endswith('.tif'):
        # Definir la ruta del archivo
        in_path = os.path.join(tiff_dir, file)

        # Definir la proyección
        arcpy.DefineProjection_management(in_path, sr)

print("Proyectado a WGS84 Global")
