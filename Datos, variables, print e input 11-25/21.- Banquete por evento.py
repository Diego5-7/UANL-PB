evento = input("Nombre del evento: ")
fecha = input("Fecha del evento: ")
asistentes = int(input("Número de asistentes: "))

agua = asistentes * 1.5          
carne = asistentes * 350         
salsa = agua * 0.25              

print("Evento:", evento)
print("Fecha:", fecha)
print("Asistentes:", asistentes)
print("Agua necesaria (litros):", agua)
print("Carne necesaria (gramos):", carne)
print("Salsa necesaria (litros):", salsa)