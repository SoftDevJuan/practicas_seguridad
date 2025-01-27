import os
import hashlib

def hash_encrypt_to_new_file(file_path):
    """Cifra el contenido de un archivo usando SHA-256 y lo guarda en un nuevo archivo en formato hexadecimal."""
    with open(file_path, "rb") as file:
        data = file.read()
    hashed_data = hashlib.sha256(data).hexdigest()
    new_file_path = file_path + ".hex"
    with open(new_file_path, "w") as new_file:
        new_file.write(hashed_data)
    print(f"Contenido del archivo '{file_path}' cifrado y guardado en '{new_file_path}'.")

def list_files():
    """Lista todos los archivos en el directorio actual."""
    files = [f for f in os.listdir() if os.path.isfile(f)]
    if files:
        print("Archivos disponibles:")
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")
    else:
        print("No hay archivos en el directorio.")
    return files

def main():
    while True:
        print("\nMenú:")
        print("1. Listar archivos")
        print("2. Cifrar un archivo (SHA-256)")
        print("3. Salir")

        try:
            option = int(input("Seleccione una opción: "))
            if option == 1:
                list_files()
            elif option == 2:
                files = list_files()
                if files:
                    file_index = int(input("Seleccione el número del archivo a cifrar: ")) - 1
                    if 0 <= file_index < len(files):
                        hash_encrypt_to_new_file(files[file_index])
                    else:
                        print("Opción inválida.")
            elif option == 3:
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()