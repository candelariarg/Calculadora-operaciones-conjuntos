def menu ():
    
def obtener_conjuntos():
    input ("Ingrese la cantidad de conjuntos (2 o 3): ")
    while numero_conjuntos not in [2, 3]:
        try:
            numero_conjuntos = int(input("Ingrese el número de conjuntos con los que desea trabajar (2 o 3): "))
            if numero_conjuntos not in [2, 3]:
                print("Por favor, ingrese 2 o 3.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    if numero_conjuntos == 2:
        print("\nHa elegido trabajar con 2 conjuntos.")
        conjunto1 = input("Ingrese el primer conjunto (ej. 'a,b,c'): ")
        conjunto2 = input("Ingrese el segundo conjunto (ej. 'd,e,f'): ")
        return [conjunto1, conjunto2]
    elif numero_conjuntos == 3:
        print("\nHa elegido trabajar con 3 conjuntos.")
        conjunto1 = input("Ingrese el primer conjunto (ej. 'a,b,c'): ")
        conjunto2 = input("Ingrese el segundo conjunto (ej. 'd,e,f'): ")
        conjunto3 = input("Ingrese el tercer conjunto (ej. 'g,h,i'): ")
        return [conjunto1, conjunto2, conjunto3]