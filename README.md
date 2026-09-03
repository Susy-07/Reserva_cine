# Reserva_cine
Estudiante: Pacheco Merino Susy Mishell
##Objetivo: Desarrollar en Python un programa que gestione la reserva de asientos de sala de cine de 3 filas y 4 columnas.
0 = Asiento libre
1 = Asiento reservado

##Cómo ejecutar.
1. Crear un archivo llamado reserva_cine.py en Visual Studio Code
2. Ejecutar el programa
3. Escribir el número de la fila (0 a 2) y columna (0 a 3)
4.El programa mostrará la sala indicando con el asiento que ha sido reservado

##Funcionamiento
- Crear una matriz 3 x 4 con todos sus valores en cero
- El programa solicita fila y columna que desean reservar 
- Se verifica que los datos estén el rango permitido
- El asiento seleccionado cambia su valor a 1 indicando que está ocupado
- Finalmente se muestra toda la sala completa  con bucles anidados
