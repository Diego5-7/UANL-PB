precio_venta = float(input("Ingrese el precio de venta por pieza: "))
cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
costo_fijo = float(input("Ingrese el costo fijo total: "))
costo_variable = float(input("Ingrese el costo variable por pieza: "))

ingreso_total = precio_venta * cantidad_vendida
costo_total = costo_fijo + (costo_variable * cantidad_vendida)

beneficio = ingreso_total - costo_total

print(f"\nEl beneficio total es: ${beneficio:.2f}")
