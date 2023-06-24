import arcpy
import os

# Directorio de entrada (rasters) y salida (vectoriales)
input_directory = r"G:\TFM\Resultados Restoration planner\P.pinaster\Pathways\only33"
output_directory = r"G:\TFM\Resultados Restoration planner\P.pinaster\Pathways\Vectoriales"

# Obtener la lista de archivos raster en el directorio de entrada
arcpy.env.workspace = input_directory
raster_list = arcpy.ListRasters("*", "TIF")

# Crear la carpeta de salida si no existe
if not arcpy.Exists(output_directory):
    arcpy.CreateFolder_management(os.path.dirname(output_directory), os.path.basename(output_directory))

# Configurar el entorno de procesamiento
arcpy.env.overwriteOutput = True

# Lista para almacenar las capas de líneas
line_layers = []

# Recorrer los archivos raster en el directorio de entrada
for raster_file in raster_list:
    # Ruta completa del archivo raster
    input_raster = os.path.join(input_directory, raster_file)

    # Crear un nombre base para los archivos de salida
    file_name = os.path.splitext(raster_file)[0]
    valid_file_name = arcpy.ValidateTableName(file_name, output_directory)

    # Convertir los píxeles a polígonos
    polygon_output = os.path.join(output_directory, valid_file_name + "_polygons.shp")
    arcpy.RasterToPolygon_conversion(input_raster, polygon_output, "NO_SIMPLIFY", "VALUE")

    # Realizar la disolución en los polígonos resultantes
    dissolve_output = os.path.join(output_directory, valid_file_name + "_dissolve.shp")
    arcpy.Dissolve_management(polygon_output, dissolve_output)

    # Crear una capa de líneas a lo largo del eje de la geometría disuelta
    lines_output = os.path.join(output_directory, valid_file_name + "_lines.shp")
    arcpy.FeatureToLine_management(dissolve_output, lines_output)

    # Crear un nuevo campo y asignar el nombre del archivo a las capas de líneas
    arcpy.AddField_management(lines_output, "FileName", "TEXT")
    with arcpy.da.UpdateCursor(lines_output, "FileName") as cursor:
        for row in cursor:
            row[0] = os.path.splitext(raster_file)[0]
            cursor.updateRow(row)

    # Agregar la capa de líneas a la lista
    line_layers.append(lines_output)

    # Eliminar los archivos resultantes que no sean capas de líneas
    arcpy.Delete_management(polygon_output)
    arcpy.Delete_management(dissolve_output)

    print("Archivo procesado: {0}".format(raster_file))

# Combinar todas las capas de líneas en un solo archivo
output_pathways = os.path.join(output_directory, "Pathways.shp")
arcpy.Merge_management(inputs=line_layers, output=output_pathways)

print("Proceso completado")
