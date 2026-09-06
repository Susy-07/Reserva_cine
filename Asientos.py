# Crear una matriz de la sala con 3 filas y 4 columnas llena de ceros
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
print("---RESERVA DE ASIENTOS DE CINE ---")

# Le pido al usuario la fila y la columna a reservar
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

# Cambio el valor del asiento a 1 para marcar la reserva
asientos[fila][columna] = 1

print("Asiento reservado")

# Uso bucles anidados para mostrar la matriz en pantalla
for fila in asientos:
    for asiento in fila:
        print(asiento, end=" ")
    print()