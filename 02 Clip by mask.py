import os
import arcpy
import arcpy.mapping as mapping

# Definir el directorio de entrada (contiene los archivos TIFF a recortar)
in_folder = r'C:\TFM\Worldclimedata_def\Future_split_comodin'

# Definir el directorio de salida (para guardar los archivos recortados)
out_folder = r'C:\TFM\Worldclimedata_def\Future_split_recortado_halepensis'

# Definir la ruta del shapefile de recorte
clip_shapefile = r'C:\TFM\Modelados Maxent\P.halepensis\study_area\study_area.shp'

# Acceder al documento actual de ArcMap
mxd = mapping.MapDocument("CURRENT")

# Acceder al marco de datos y a la tabla de contenido
df = mapping.ListDataFrames(mxd)[0]
layers = mapping.ListLayers(mxd, "", df)

# Recorrer cada carpeta dentro del directorio de entrada
for root, dirs, files in os.walk(in_folder):
    # Crear la ruta de salida correspondiente a la carpeta actual
    out_folder_path = root.replace(in_folder, out_folder)
    if not os.path.exists(out_folder_path):
        os.makedirs(out_folder_path)

     # Recorrer cada archivo TIFF dentro de la carpeta actual
    for filename in files:
        if filename.endswith('.tif'):
            # Definir la ruta completa del archivo de entrada y salida
            in_path = os.path.join(root, filename)
            out_path = os.path.join(out_folder_path, filename)

            # Realizar el recorte utilizando la herramienta "Clip" de ArcGIS
            arcpy.Clip_management(in_path, "#", out_path, clip_shapefile, "0", "ClippingGeometry")

            # Eliminar la capa recortada de la tabla de contenidos
            lyr = arcpy.mapping.Layer(out_path)
            arcpy.mapping.RemoveLayer(df, lyr)

            print("Archivo recortado y eliminado de la tabla de contenidos: " + out_path)

