clave = input("Crea tu contraseña: ")
intentos = 0
confirmar = input("Vuelve a escribir tu contraseña: ")

while confirmar != clave and intentos < 2:
    print("Las contraseñas no coinciden.")
    intentos += 1
    confirmar = input("Vuelve a escribir tu contraseña: ")

if confirmar == clave:
    print("Contraseña confirmada.")
else:
    print("Cuenta cancelada")
