import os
import zipfile

def unzip_all_files(folder_path):
    """
    Descomprime todos los archivos .zip que se encuentran en una carpeta y sus subcarpetas.
    """
    found_zips = False
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.zip'):
                found_zips = True
                filepath = os.path.join(root, filename)
                with zipfile.ZipFile(filepath, 'r') as zip_ref:
                    zip_ref.extractall(root)
                os.remove(filepath)
    if not found_zips:
        print("No se encontraron archivos .zip en la carpeta y sus subcarpetas.")

def main():
    """
    Función principal del script.
    """
    # Pide al usuario que ingrese la ruta a la carpeta que desea descomprimir
    folder_path = input("Ingrese la ruta a la carpeta que desea descomprimir: ")
    
    # Verifica que la ruta ingresada existe
    if not os.path.isdir(folder_path):
        print("La ruta ingresada no es una carpeta existente.")
        return
    
    # Descomprime los archivos .zip en la carpeta y sus subcarpetas
    unzip_all_files(folder_path)
    print("Descompresión completada.")

if __name__ == '__main__':
    main()