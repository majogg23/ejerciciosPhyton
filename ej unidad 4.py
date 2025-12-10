
#ej1programacion:
def esta_ordenada_creciente(lista):
    return all(lista[i] <= lista[i+1] for i in range(len(lista) - 1))

def esta_ordenada_decreciente(lista):
    return all(lista[i] >= lista[i+1] for i in range(len(lista) - 1))

def es_gaspariforme(lista):
    suma_parcial = 0
    for x in lista:
        suma_parcial += x
        if suma_parcial < 0:
            return False
    return suma_parcial == 0

def es_melchoriforme(lista):
    total = sum(lista)
    return any(2*x == total for x in lista)

# Ejemplo de prueba
a = [2, 4, 6]
print("Ordenada crecientemente:", esta_ordenada_creciente(a))
print("Ordenada decrecientemente:", esta_ordenada_decreciente(a))
print("Gaspariforme:", es_gaspariforme(a))
print("Melchoriforme:", es_melchoriforme(a))

#ej2matrices
# Definís la matriz escribiendo cada fila como una lista
matriz = []
matriz.append([0, 0, 0, 0, 1])
matriz.append([0, 0, 0, 1, 2])
matriz.append([0, 0, 1, 2, 3])
matriz.append([0, 1, 2, 3, 4])
matriz.append([1, 2, 3, 4, 5])

# Función para mostrarla
def mostrarMat(a):
    for fila in a:
        for valor in fila:
            print(valor, end=' ')
        print()


mostrarMat(matriz)
#ej3unidad4

def buscar_posicion(lista, x):
    if x in lista:
        return lista.index(x)  # Retorna la primera posición
    else:
        return -1

# Función que cuenta cuántas veces aparece x en la lista
def contar_apariciones(lista, x):
    return lista.count(x)

# Función que verifica si x aparece más veces que el valor máximo de la lista
def x_mas_frecuente_que_max(lista, x):
    if not lista:
        return False
    max_valor = max(lista)
    return lista.count(x) > lista.count(max_valor)

# Programa principal
n = int(input("Cuántos números vas a ingresar?: "))
vector = []

for _ in range(n):
    num = int(input("Ingrese un número entero: "))
    vector.append(num)

x = int(input("Ingrese el valor a buscar: "))

posicion = buscar_posicion(vector, x)
apariciones = contar_apariciones(vector, x)
mas_frecuente = x_mas_frecuente_que_max(vector, x)

print(f"La posición de {x} en el vector es: {posicion}")
print(f"El valor {x} aparece {apariciones} veces.")
print(f"¿El valor {x} aparece más veces que el valor mayor del vector?: {mas_frecuente}")

#ej4
def calcular_media(vector):
    if len(vector) == 0:
        return 0  # evitar división por cero
    suma = sum(vector)
    media = suma / len(vector)
    return media

# Ejemplo de uso
numeros = [4, 8, 6, 2, 10]
print("La media es:", calcular_media(numeros))

#ej5
def esTelescopio(n, vec):
    for i in range(len(vec) - 1):
        if vec[i] > vec[i + 1]:
            return False

    # Verificar que cada número i entre 1 y n aparece exactamente i veces
    for i in range(1, n + 1):
        if vec.count(i) != i:
            return False
        return True



import numpy as np


