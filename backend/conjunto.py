def obtener_conjuntos():
    while True:
        try:
            numero_conjuntos = int(input("Ingrese el número de conjuntos con los que desea trabajar (2 o 3): "))
            if numero_conjuntos in [2, 3]:
                break
            else:
                print("Por favor, ingrese 2 o 3.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    conjuntos = []
    for i in range(1, numero_conjuntos + 1):
        conjunto = input(f"Ingrese el conjunto {i} (ej. 'a,b,c'): ")
        conjuntos.append([elem.strip() for elem in conjunto.split(",")])
    return conjuntos
