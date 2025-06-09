from backend.conjunto import obtener_conjuntos

def main():
    conjuntos = obtener_conjuntos()
    set1 = set(conjuntos[0])
    set2 = set(conjuntos[1])

    while True:
        print("Operaciones disponibles:")
        print("1. Unión")
        print("2. Intersección")
        print("3. Diferencia (A - B)")
        print("4. Diferencia (B - A)")
        print("5. Diferencia simétrica (A Δ B)")
        print("6. Complemento de A")
        print("7. Complemento de B")
        print("8. Salir")
        opcion = input("Elija una operación (1/2/3/4/5/6/7/8): ")

        if opcion == "1":
            resultado = set1.union(set2)
            print("Unión:", resultado)
        elif opcion == "2":
            resultado = set1.intersection(set2)
            print("Intersección:", resultado)
        elif opcion == "3":
            resultado = set1.difference(set2)
            print("Diferencia (A - B):", resultado)
        elif opcion == "4":
            resultado = set2.difference(set1)
            print("Diferencia (B - A):", resultado)
        elif opcion == "5":
            resultado = set1.symmetric_difference(set2)
            print("Diferencia simétrica (A Δ B):", resultado)
        elif opcion == "6":
            universo = set(input("Ingrese el universo (ej. 'a,b,c,d'): ").split(","))
            resultado = universo.difference(set1)
            print("Complemento de A:", resultado)
        elif opcion == "7":
            universo = set(input("Ingrese el universo (ej. 'a,b,c,d'): ").split(","))
            resultado = universo.difference(set2)
            print("Complemento de B:", resultado)
        elif opcion == "8":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()