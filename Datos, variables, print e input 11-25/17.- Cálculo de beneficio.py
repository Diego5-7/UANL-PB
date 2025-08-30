precio_venta = float(input("Ingresa el precio de venta por pieza: "))
cantidad = int(input("Ingresa la cantidad vendida: "))
costo_fijo = float(input("Ingresa el costo fijo: "))
costo_variable = float(input("Ingresa el costo variable por pieza: "))

ingreso_total = precio_venta * cantidad

costo_total = costo_fijo + (costo_variable * cantidad)

beneficio = ingreso_total - costo_total

print("El beneficio total es: $", beneficio)
