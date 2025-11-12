import re

correo = input("Ingresa un correo: ")

if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
    print("Válido")
else:
    print("Inválido")
