try:
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    carrera = input("Carrera: ")

    with open("perfil.txt", "w") as f:
        f.write(nombre + "\n")
        f.write(edad + "\n")
        f.write(carrera + "\n")

    print("Datos guardados en perfil.txt")
except Exception as e:
    print("Error al guardar:", e)
