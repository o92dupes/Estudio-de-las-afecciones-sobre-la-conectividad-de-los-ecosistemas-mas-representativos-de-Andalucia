import os
import shutil

# Ruta de la carpeta de entrada
input_folder = r"C:\TFM\Worldclimedata_def\Future_split_recortado_pinaster"

# Ruta de la carpeta de salida
output_folder = r"C:\TFM\Worldclimedata_def\Future_selected_variables_pinaster"

# Nombres de los archivos a seleccionar
selected_files = ["bio1.tif", "bio3.tif", "bio4.tif", "bio13.tif","bio15.tif"]

# Recorre las carpetas y copia los archivos seleccionados a la carpeta de salida
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file in selected_files:
            file_path = os.path.join(root, file)
            output_path = os.path.join(output_folder, os.path.relpath(file_path, input_folder))
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            shutil.copy(file_path, output_path)
            print("Archivo {} copiado a {}".format(file_path, output_path))
