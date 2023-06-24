import os
import rasterio

# Directorio de entrada
input_folder = r"C:\TFM\Worldclimedata_def\Historical_clipped_ilex"
# Directorio de salida
output_folder = r"C:\TFM\Modelados Maxent\Q.ilex\Current_ASCII"

# Recorre todas las carpetas del directorio de entrada
for dirpath, dirnames, filenames in os.walk(input_folder):
    # Crea una carpeta de salida con la misma estructura que la carpeta de entrada
    output_dir = os.path.join(output_folder, os.path.relpath(dirpath, input_folder))
    os.makedirs(output_dir, exist_ok=True)

    # Recorre todos los archivos de la carpeta actual
    for file in filenames:
        if file.endswith(".tif"):
            # Abre el archivo raster
            input_file = os.path.join(dirpath, file)
            with rasterio.open(input_file) as src:
                # Lee los datos del raster y guarda la información de tamaño y resolución
                data = src.read(1)
                size = src.shape
                transform = src.transform

            # Crea el archivo ASCII y escribe los datos
            output_file = os.path.join(output_dir, os.path.splitext(file)[0] + ".asc")
            with open(output_file, "w") as f:
                # Escribe la cabecera del archivo
                f.write("ncols {}\n".format(size[1]))
                f.write("nrows {}\n".format(size[0]))
                f.write("xllcorner {}\n".format(transform[2]))
                f.write("yllcorner {}\n".format(transform[5] + (size[0] * transform[4])))
                f.write("cellsize {}\n".format(transform[0]))
                f.write("NODATA_value -9999\n")
                
                # Escribe los datos del raster en filas
                for row in range(size[0]):
                    for col in range(size[1]):
                        value = data[row, col]
                        if value == src.nodata:
                            f.write("-9999 ")
                        else:
                            f.write("{} ".format(value))
                    f.write("\n")
                    
            print("Archivo {} convertido a ASCII".format(input_file))
