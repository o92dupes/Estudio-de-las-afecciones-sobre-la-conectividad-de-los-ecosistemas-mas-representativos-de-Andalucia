import os

folder_path = r"C:\TFM\Modelados Maxent\P.halepensis\Current_ASCII"

# Recorre los archivos en la carpeta de entrada y modifica el valor de las comas
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r') as file:
        contents = file.read()
    contents = contents.replace(',', '.')
    with open(file_path, 'w') as file:
        file.write(contents)
    print("Archivo {} modificado".format(file_path))
