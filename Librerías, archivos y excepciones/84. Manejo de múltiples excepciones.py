nombre = input("Nombre del archivo: ")

try:
    with open(nombre, "r") as f:
        contenido = f.read(5)
        numero = int(contenido)
        print("Número leído:", numero)
except FileNotFoundError:
    print("Error: El archivo no existe.")
except ValueError:
    print("Error: Los primeros 5 caracteres no son un número entero.")
except Exception as e:
    print("Error desconocido:", e)
