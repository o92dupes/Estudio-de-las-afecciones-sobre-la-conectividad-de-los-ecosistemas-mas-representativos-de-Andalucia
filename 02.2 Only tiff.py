import os

folder_path = r"C:\TFM\Worldclimedata_def\Future_split_recortado_halepensis"

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        if not file_path.lower().endswith(".tif"):
            os.remove(file_path)
            print(f"Archivo eliminado: {file_path}")
