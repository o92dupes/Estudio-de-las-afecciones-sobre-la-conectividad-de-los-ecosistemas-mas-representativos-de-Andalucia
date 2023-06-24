import os

folder_path = r"C:\TFM\Worldclimedata_def\Historical_clipped_halepensis"

files_to_delete = ["bio8.tif", "bio9.tif", "bio18.tif", "bio19.tif"]

for file in files_to_delete:
    file_path = os.path.join(folder_path, file)
    if os.path.exists(file_path):
        os.remove(file_path)
        print("Archivo {} eliminado".format(file_path))
    else:
        print("El archivo {} no existe".format(file_path))
