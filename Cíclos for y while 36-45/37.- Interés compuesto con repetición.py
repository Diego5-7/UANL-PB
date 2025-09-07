while True:
    C = float(input("Introduce el capital inicial (C): "))
    i = float(input("Introduce la tasa de interés (i) en formato decimal: "))
    n = int(input("Introduce el número de periodos (n): "))
    
    M = C * (1 + i) ** n
    
    print(f"El monto final después de {n} periodos es: {M}")
    respuesta = input("¿Quieres hacer otro cálculo? (sí/no): ").lower()
    
    if respuesta != "sí":
        break 
