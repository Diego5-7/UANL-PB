edad = int(input("Ingresa tu edad: "))

if edad < 0 or edad > 120:
    print("Edad inválida")
elif edad < 10:
    print("Niño")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Joven")
elif edad < 60:
    print("Adulto")
else:
    print("Adulto mayor")

if edad >= 18 and edad <= 120:
    print("Eres mayor de edad")
