from backend.conjunto import obtener_conjuntos

def obtener_universo():
    print("\nDefina el conjunto universal.")
    print("Presione Enter para usar el universo por defecto: {0,1,2,3,4,5,6,7,8,9,10}")
    print("O ingrese una expresión como: 0,1,2,3,4,5,6,7,8,9,10")
    expr = input("Universo: ").strip()
    if expr == "":
        return set(str(i) for i in range(11))
    else:
        elementos = [e.strip() for e in expr.split(",") if e.strip() != ""]
        if not elementos:
            print("Expresión inválida. Usando universo por defecto.")
            return set(str(i) for i in range(11))
        return set(elementos)

def main():
    conjuntos = obtener_conjuntos()
    set1 = set(conjuntos[0])
    set2 = set(conjuntos[1])

    # Mensaje si algún conjunto está vacío
    if not set1:
        print("Advertencia: El conjunto A está vacío.")
    if not set2:
        print("Advertencia: El conjunto B está vacío.")

    while True:
        print("\nOperaciones disponibles:")
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
            if not resultado:
                print("Resultado: conjunto vacío.")
            else:
                print("Unión:", resultado)
        elif opcion == "2":
            resultado = set1.intersection(set2)
            if not resultado:
                print("No hay intersección (conjunto vacío).")
            else:
                print("Intersección:", resultado)
        elif opcion == "3":
            resultado = set1.difference(set2)
            if not resultado:
                print("Resultado: conjunto vacío.")
            else:
                print("Diferencia (A - B):", resultado)
        elif opcion == "4":
            resultado = set2.difference(set1)
            if not resultado:
                print("Resultado: conjunto vacío.")
            else:
                print("Diferencia (B - A):", resultado)
        elif opcion == "5":
            resultado = set1.symmetric_difference(set2)
            if not resultado:
                print("Resultado: conjunto vacío.")
            else:
                print("Diferencia simétrica (A Δ B):", resultado)
        elif opcion == "6":
            universo = obtener_universo()
            resultado = universo.difference(set1)
            if not resultado:
                print("El complemento de A es el conjunto vacío.")
            else:
                print("Complemento de A:", resultado)
        elif opcion == "7":
            universo = obtener_universo()
            resultado = universo.difference(set2)
            if not resultado:
                print("El complemento de B es el conjunto vacío.")
            else:
                print("Complemento de B:", resultado)
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()