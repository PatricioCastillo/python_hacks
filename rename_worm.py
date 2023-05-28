import os

ruta = r"C:\Users\Dash\Desktop\Unidad II"

def cambiar_nombre_archivos(ruta):
    contador = 1
    for archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, archivo)
        if os.path.isfile(ruta_completa):
            nombre, extension = os.path.splitext(archivo)
            nuevo_nombre = "INFECTADO" + str(contador) + extension
            contador += 1
            nuevo_nombre_completo = os.path.join(ruta, nuevo_nombre)
            os.rename(ruta_completa, nuevo_nombre_completo)

cambiar_nombre_archivos(ruta)
print("Nombres de archivos cambiados con éxito.")
