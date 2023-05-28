import os
import itertools

# Definir el nombre base para los directorios
nombre_base = "directorio"

# Ruta donde se crearán los directorios
ruta_base = "C:/Users/Dash/Desktop/virus"

# Crear los directorios en un ciclo for infinito
for i in itertools.count():
    # Crear el nombre del directorio
    nombre_directorio = f"{nombre_base}{i}"

    # Ruta completa del directorio
    ruta_directorio = os.path.join(ruta_base, nombre_directorio)

    # Crear el directorio
    os.makedirs(ruta_directorio)

    print(f"Directorio {nombre_directorio} creado en {ruta_directorio}")
