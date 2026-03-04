# ejercicio_08.py

# Título del Ejercicio: Iteración de Colecciones

# Descripción del Problema:
# Recorrer una lista y un diccionario aplicando condiciones.

# Requisito:
# 1. Recorrer lista con for.
# 2. Aplicar condición.
# 3. Crear nueva lista.
# 4. Recorrer diccionario.

# Escribe tu codigo dejajo de esta línea:

lista_numeros = [1, 2, 3, 4, 5]
nueva_lista = []

for numero in lista_numeros:
    if numero % 2 == 0:
        nueva_lista.append(numero * 2)

print("Nueva lista:", nueva_lista)

diccionario_personas = {
    "Ana": 17,
    "Luis": 20,
    "Carlos": 15
}

for nombre, edad in diccionario_personas.items():
    if edad >= 18:
        print(f"{nombre} es mayor de edad")
    else:
        print(f"{nombre} es menor de edad")