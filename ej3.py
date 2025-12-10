
#ej3unidad4

def buscar_posicion(l, x):
    if x in l:
        return l.index(x)  
        return -1

def contar_apariciones(l, x):
    return l.count(x)


def mas_veces(l, x):
    if not l:
        return False
    max_valor = max(l)
    return l.count(x) > l.count(max_valor)


n = int(input("Cuántos números vas a ingresar?: "))
vec = []

for _ in range(n):
    num = int(input("Ingrese un número entero: "))
    vec.append(num)

x = int(input("Ingrese el valor a buscar: "))

posicion = buscar_posicion(vec, x)
apariciones = contar_apariciones(vec, x)
mas_frecuente = mas_veces(vec, x)

print(f"La posición de {x} en el vector es: {posicion}")
print(f"El valor {x} aparece {apariciones} veces.")
print(f"¿El valor {x} aparece más veces que el valor mayor del vector?: {mas_frecuente}")