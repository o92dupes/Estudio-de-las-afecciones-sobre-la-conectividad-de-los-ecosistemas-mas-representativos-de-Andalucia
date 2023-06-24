import arcpy

# Establecer entorno de trabajo
arcpy.env.workspace = r"C:\TFM\Modelados Maxent\Q.suber\current"

# Obtener lista de rasters en el directorio
raster_list = arcpy.ListRasters()

# Definir parámetros para la estadística focal
neighborhood = arcpy.sa.NbrRectangle(3, 3, "CELL")  # Vecindario de 3x3 celdas

# Ruta de salida para los rasters rellenados
output_folder = r"C:\TFM\Modelados Maxent\Q.suber\current reescalados"

# Verificar si la carpeta de salida existe, si no, crearla
if not arcpy.Exists(output_folder):
    arcpy.CreateFolder_management(arcpy.env.workspace, "Filled")

# Recorrer la lista de rasters y aplicar la estadística focal
for raster_name in raster_list:
    raster_path = arcpy.env.workspace + "\\" + raster_name
    
    # Crear objeto Raster a partir del archivo
    raster = arcpy.Raster(raster_path)
    
    # Crear una máscara para los valores NaN
    mask = arcpy.sa.IsNull(raster)
    
    # Rellenar valores NaN utilizando la estadística focal (media)
    filled_raster = arcpy.sa.Con(mask, arcpy.sa.FocalStatistics(raster, neighborhood, "MEAN"))
    
    # Aplicar la máscara para preservar los valores existentes en el raster original
    output_raster = arcpy.sa.Con(mask, filled_raster, raster)
    
    # Guardar el raster rellenado en la carpeta de salida
    output_path = output_folder + "\\" + raster_name
    output_raster.save(output_path)
    
    print("Relleno completado para el raster: " + raster_name)
