asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
print("---RESERVA DE ASIENTOS DE CINE ---")
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))
asientos[fila][columna] = 1

print("Asiento reservado")
print("Reserva de asientos:")
for fila in asientos:
    for asiento in fila:
        print(asiento, end=" ")
    print()

