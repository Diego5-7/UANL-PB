capital = float(input("Capital inicial: "))
tasa = float(input("Tasa de interés anual (%): ")) / 100
periodos = int(input("Número de periodos (años): "))

interes_simple = capital * (1 + tasa * periodos)
interes_compuesto = capital * (1 + tasa) ** periodos

print("Capital final con interés simple:", interes_simple)
print("Capital final con interés compuesto:", interes_compuesto)