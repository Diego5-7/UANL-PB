def es_valido(email):
    return "@" in email

# Ejemplo
correo = input("Ingresa tu correo: ")
if es_valido(correo):
    print("Correo válido")
else:
    print("Correo inválido")