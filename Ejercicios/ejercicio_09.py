# ejercicio_09.py

# Título del Ejercicio: Input Avanzado y Formateo

# Descripción del Problema:
# Solicitar múltiples datos y combinarlos usando f-strings.

# Requisito:
# 1. Pedir nombre.
# 2. Pedir edad.
# 3. Pedir ciudad.
# 4. Usar f-string.
# 5. Multiplicar texto.

# Escribe tu codigo dejajo de esta línea:

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
ciudad = input("Ingresa tu ciudad: ")

mensaje = f"Hola {nombre}, tienes {edad} años y vives en {ciudad}."
print(mensaje)

print("Bienvenido! " * 3)