import os
import arcpy
import shutil

# Definir el directorio de entrada (contiene los archivos ASCII)
in_folder = r'C:\TFM\Modelados Maxent\P.halepensis\Final_models_2'

# Crear el directorio de salida para los archivos seleccionados
out_folder = r'C:\TFM\Modelados Maxent\P.halepensis\avg_2'
if not os.path.exists(out_folder):
    os.makedirs(out_folder)

# Crear el directorio de salida para los archivos TIFF
tiff_dir = r'C:\TFM\Modelados Maxent\P.halepensis\avg_TIFF_2'
if not os.path.exists(tiff_dir):
    os.makedirs(tiff_dir)

# Seleccionar todos los archivos ASCII que terminen en '_avg'
for root, dirs, files in os.walk(in_folder):
    for file in files:
        if file.endswith('_avg.asc'):
            # Copiar el archivo al directorio de salida
            in_path = os.path.join(root, file)
            out_path = os.path.join(out_folder, file)
            shutil.copy(in_path, out_path)
            

# Convertir los archivos ASCII a TIFF y guardarlos en el directorio de salida para TIFF
for file in os.listdir(out_folder):
    if file.endswith('.asc'):
        # Definir la ruta de entrada y salida
        in_path = os.path.join(out_folder, file)
        out_path = os.path.join(tiff_dir, file.replace('.asc', '.tif'))

        # Convertir el archivo a TIFF
        arcpy.ASCIIToRaster_conversion(in_path, out_path, "FLOAT")

        

# Definir la proyección de los archivos TIFF y guardarlos en el directorio para TIFF proyectados
sr = arcpy.SpatialReference('WGS 1984 UTM Zone 30N')

for file in os.listdir(tiff_dir):
    if file.endswith('.tif'):
        # Definir la ruta del archivo
        in_path = os.path.join(tiff_dir, file)

        # Definir la proyección
        arcpy.DefineProjection_management(in_path, sr)

        

# Eliminar todos los archivos que no sean TIFF
for file in os.listdir(tiff_dir):
    if not file.endswith('.tif'):
        os.remove(os.path.join(tiff_dir, file))

print("Eliminados todos los archivos que no son TIFF.")
