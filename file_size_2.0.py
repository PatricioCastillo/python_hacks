import os
import random
import string

# Tamaño objetivo de cada archivo en bytes (10 MB)
tamanio_objetivo = 100 * 1024 * 1024

# Genera una cadena de caracteres aleatorios
contenido = ''.join(random.choices(string.ascii_letters + string.digits, k=tamanio_objetivo))

# Ruta donde se generarán los archivos
ruta = r"C:\Users\Dash\Desktop\file"

# Crea los 5 archivos
for i in range(5):
    nombre_archivo = f"archivo_{i+1}.txt"
    ruta_archivo = os.path.join(ruta, nombre_archivo)

    # Escribe el contenido en el archivo
    with open(ruta_archivo, "w") as archivo:
        archivo.write(contenido)

    print(f"Archivo generado: {ruta_archivo}")

print("Proceso completado.")
