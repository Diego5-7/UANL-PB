clave = input("Crea tu contraseña: ")
confirmar = input("Vuelve a escribir tu contraseña: ")

while confirmar != clave:
    print("Las contraseñas no coinciden. Intenta de nuevo.")
    confirmar = input("Vuelve a escribir tu contraseña: ")

print("Contraseña confirmada.")
