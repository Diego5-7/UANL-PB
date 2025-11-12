import re

texto = input("Escribe varios correos: ")
usuarios = re.findall(r'([\w\.-]+)@[\w\.-]+\.\w+', texto)
print("Usuarios encontrados:", usuarios)
