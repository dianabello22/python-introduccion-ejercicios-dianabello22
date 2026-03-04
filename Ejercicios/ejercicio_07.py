# ejercicio_07.py

# Título del Ejercicio: Input y Casting

# Descripción del Problema:
# Solicitar números al usuario, convertirlos y realizar operaciones.

# Requisito:
# 1. Pedir número entero.
# 2. Pedir número decimal.
# 3. Convertir con int() y float().
# 4. Mostrar resultados.

# Escribe tu codigo dejajo de esta línea:

numero_entero = int(input("Ingresa un número entero: "))
numero_decimal = float(input("Ingresa un número decimal: "))

suma = numero_entero + numero_decimal
multiplicacion = numero_entero * numero_decimal

print(f"Suma: {suma}")
print(f"Multiplicación: {multiplicacion}")