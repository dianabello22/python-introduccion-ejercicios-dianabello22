# ejercicio_05.py

# Título del Ejercicio: ciclos

# Descripción del Problema:
# Crear un programa que cuente del 1 al 3 usando un ciclo for
# y calcule la suma de esos números.

# Requisito:
# 1. Usar ciclo for.
# 2. Mostrar cada número.
# 3. Calcular suma acumulada.

# Ejemplo de Salida Esperada:
# Número: 1
# Número: 2
# Número: 3
# Suma total: 6

# Escribe tu codigo dejajo de esta línea:

suma_total = 0

for numero in range(1, 4):
    print("Número:", numero)
    suma_total += numero

print("Suma total:", suma_total)