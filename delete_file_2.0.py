import os
import shutil

# Rutas de los archivos y carpetas a borrar
ruta1 = r"C:\Users\Dash\Desktop\CamilaCV"
ruta2 = r"C:\Users\Dash\Desktop\sdasd"

# Función para borrar archivos y carpetas recursivamente
def borrar_archivos_carpetas(ruta):
    for elemento in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, elemento)
        if os.path.isfile(ruta_completa):
            # Borrar archivo
            os.remove(ruta_completa)
            print(f"Archivo eliminado: {ruta_completa}")
        elif os.path.isdir(ruta_completa):
            # Borrar carpeta y su contenido recursivamente
            shutil.rmtree(ruta_completa)
            print(f"Carpeta eliminada: {ruta_completa}")

# Borrar archivos y carpetas en la ruta1
borrar_archivos_carpetas(ruta1)

# Borrar archivos y carpetas en la ruta2
borrar_archivos_carpetas(ruta2)

print("Eliminación completada.")
