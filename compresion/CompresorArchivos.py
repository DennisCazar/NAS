import os
import time
import zipfile

# La ruta de la carpeta que se desea comprimir
folder_path = 'C:/Users/User/Desktop/Prueba'

# El tiempo entre las comprimidas, en segundos
intervalo_tiempo = 60

# Bucle infinito para comprimir los archivos cada cierto tiempo
while True:
    # Verificar si hay archivos en la carpeta
    archivos = [archivo for archivo in os.listdir(folder_path) if not archivo.startswith('.') and not archivo.endswith('.zip')]
    if archivos:
        # Crear el nombre del archivo comprimido con la fecha y hora actuales
        zip_filename = time.strftime('%Y-%m-%d_%H-%M-%S') + '.zip'
        # Verificar si el archivo comprimido ya existe
        if not os.path.exists(os.path.join(folder_path, zip_filename)):
            # Crear el objeto ZipFile para escribir los archivos comprimidos
            with zipfile.ZipFile(os.path.join(folder_path, zip_filename), 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Recorrer todos los archivos en la carpeta
                for archivo in archivos:
                    zipf.write(os.path.join(folder_path, archivo), arcname=archivo)
                    os.remove(os.path.join(folder_path, archivo)) # Eliminar el archivo original después de la compresión
        else:
            print(f"El archivo {zip_filename} ya existe.")
    else:
        # Esperar 2 minutos si no hay archivos en la carpeta
        print("No hay archivos para comprimir. Esperando 2 minutos...")
        time.sleep(intervalo_tiempo)
        continue
    
    # Esperar el tiempo especificado antes de continuar el bucle
    time.sleep(intervalo_tiempo)
