# ejercicio_04.py

# Título del Ejercicio: Condicionales

# Descripción del Problema:
# Determina si un número es positivo, par y si una persona es mayor de edad.

# Requisitos:
# 1. Usar if, elif y else.
# 2. Evaluar número positivo.
# 3. Evaluar número par.
# 4. Evaluar mayoría de edad.

# Escribe tu codigo dejajo de esta línea:

numero = int(input("Ingresa un número: "))
edad = int(input("Ingresa tu edad: "))

if numero > 0:
    print("El número es positivo")
elif numero == 0:
    print("El número es cero")
else:
    print("El número es negativo")

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")