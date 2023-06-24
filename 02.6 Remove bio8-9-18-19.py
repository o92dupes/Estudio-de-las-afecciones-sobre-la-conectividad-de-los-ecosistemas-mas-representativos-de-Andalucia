import os

# Ruta base donde se encuentran las carpetas
base_path = "C:/TFM/Worldclimedata_def/Future_split_recortado_halepensis"

# Archivos a eliminar
files_to_delete = ["bio8", "bio9", "bio18", "bio19"]

# Función para eliminar los archivos en una carpeta específica
def delete_files(folder_path):
    for file in files_to_delete:
        file_path = os.path.join(folder_path, file + ".tif")
        if os.path.isfile(file_path):
            os.remove(file_path)

# Recorrer todas las carpetas en la ruta base y eliminar los archivos
for root, dirs, files in os.walk(base_path):
    for dir in dirs:
        folder_path = os.path.join(root, dir)
        delete_files(folder_path)

print("Proceso terminado")
