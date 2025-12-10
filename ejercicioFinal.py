
#ejercicioFinal 
#Gomez Maria Jose 

productos = [
    {"A101": {"vencimiento": (5, 2025), "calidad": True}},
    {"B220": {"vencimiento": (3, 2024), "calidad": False}},
    {"C333": {"vencimiento": (12, 2026), "calidad": True}},
    {"D777": {"vencimiento": (1, 2023), "calidad": False}}
]

def eliminar_no_aprobados(lista_productos):
    eliminados = []
    aprobados = []

    for elemento in lista_productos:
        codigo = list(elemento.keys())[0]
        info = elemento[codigo]

        if not info["calidad"]:
            eliminados.append({codigo: info})
        else:
            aprobados.append({codigo: info})

    return eliminados

productos_eliminados = eliminar_no_aprobados(productos)
print(productos_eliminados)


