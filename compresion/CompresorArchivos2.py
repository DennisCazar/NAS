import os
import time
import zipfile


def listar_archivos(folder_path):
    """
    Retorna una lista de archivos en la carpeta especificada, excluyendo 
    los archivos .zip y aquellos que comienzan con '.'.

    1. Obtiene una lista de todos los archivos en la carpeta especificada
    2. Crea una nueva lista que solo contenga los archivos que cumplan las condiciones: 
        1) que no empiece con '.' 2) que no termine con '.zip'

    Uso una list comprehension para expresar esas lineas de codigo
    """
    archivos = [archivo for archivo in os.listdir(folder_path) if not archivo.startswith('.') and not archivo.endswith('.zip')]
    return archivos



def nombre_archivoZIP():
    """
    Crea un nombre para el archivo zip a partir de la fecha y hora actuales.
    Year-Mes-Dia_Hora-Minutos-Segundos
    """
    zip_filename = time.strftime('%Y-%m-%d_%H-%M-%S') + '.zip'
    return zip_filename


def comprimir_archivos(folder_path, archivos):
    """
    Comprime los archivos especificados en un archivo zip con el nombre generado a partir de la fecha y hora actuales. 
    Los archivos originales se eliminan después de la compresión.
    """
    zip_filename = nombre_archivoZIP()
    # Verificar si el archivo comprimido ya existe
    if not os.path.exists(os.path.join(folder_path, zip_filename)):
        # Crear el objeto ZipFile para escribir los archivos comprimidos
        with zipfile.ZipFile(os.path.join(folder_path, zip_filename), 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Recorrer todos los archivos en la carpeta
            for archivo in archivos:
                zipf.write(os.path.join(folder_path, archivo), arcname=archivo)
                eliminar_archivo(os.path.join(folder_path, archivo)) # Eliminar el archivo original después de la compresión
    else:
        print(f"El archivo {zip_filename} ya existe.")


def eliminar_archivo(archivo_path):
    """
    Elimina el archivo especificado.
    """
    os.remove(archivo_path)


def esperar_tiempo(intervalo_tiempo):
    """
    Espera el tiempo especificado.
    """
    time.sleep(intervalo_tiempo)


def main():
    # La ruta de la carpeta que se desea comprimir
    folder_path = 'C:/Users/User/Desktop/Prueba'

    # El tiempo entre las comprimidas, en segundos
    intervalo_tiempo = 60

    while True:
        archivos = listar_archivos(folder_path)
        if archivos:
            comprimir_archivos(folder_path, archivos)
        else:
            # Esperar el tiempo especificado antes de continuar el bucle
            print("No hay archivos para comprimir. Esperando 2 minutos...")
            esperar_tiempo(intervalo_tiempo)
            continue

        # Esperar el tiempo especificado antes de continuar el bucle
        esperar_tiempo(intervalo_tiempo)


if __name__ == '__main__':
    main()

