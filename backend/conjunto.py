def obtener_conjuntos():
    print("Trabajará con 2 conjuntos.")
    conjuntos = []
    for i in range(1, 3):
        conjunto = input(f"Ingrese el conjunto {i} (ej. 'a,b,c'): ")
        conjuntos.append([elem.strip() for elem in conjunto.split(",")])
    return conjuntos
