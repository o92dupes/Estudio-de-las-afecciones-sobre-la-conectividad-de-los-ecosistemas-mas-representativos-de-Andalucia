import os
import rioxarray as rxr
# Solo es necesario cambiar el directorio de entrada y de salida
# Directorio de entrada
input_folder = r"C:\TFM\Worldclimedata_def\Future"
# Directorio de salida
output_folder = r"C:\TFM\Worldclimedata_def\Future_split"

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
            with rxr.open_rasterio(input_file) as src_xr:
                # Separa el raster en sus variables climáticas
                for i in range(19):
                    output_file = os.path.join(output_dir, f"bio{i+1}.tif")
                    var_data = src_xr.isel(band=i)
                    # Elimina la propiedad "long_name" para evitar el error
                    var_data.attrs.pop("long_name", None)
                    var_data.rio.to_raster(output_file)
