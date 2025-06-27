from backend.conjunto import obtener_conjuntos
import string
from matplotlib_venn import venn2
import matplotlib.pyplot as plt

def obtener_universo():
    print("\nDefina el conjunto universal.")
    print("1. Usar universo por defecto: {0,1,2,3,4,5,6,7,8,9,10}")
    print("2. Usar universo de letras: {A,B,C,...,Z}")
    print("3. Ingresar universo personalizado (ejemplo: 0,1,2,3,4,5,6,7,8,9,10)")
    opcion = input("Elija una opción (1/2/3): ").strip()
    if opcion == "1":
        return set(str(i) for i in range(11))
    elif opcion == "2":
        return set(string.ascii_uppercase)
    elif opcion == "3":
        expr = input("Ingrese los elementos separados por coma: ").strip()
        elementos = [e.strip() for e in expr.split(",") if e.strip() != ""]
        if not elementos:
            print("Expresión inválida. Usando universo por defecto.")
            return set(str(i) for i in range(11))
        return set(elementos)
    else:
        print("Opción inválida. Usando universo por defecto.")
        return set(str(i) for i in range(11))

def mostrar_venn(set1, set2, operacion):
    plt.figure(figsize=(6,6))
    v = venn2([set1, set2], set_labels=('A', 'B'))
    if operacion == "1":
        plt.title("Unión de A y B")
    elif operacion == "2":
        plt.title("Intersección de A y B")
    elif operacion == "3":
        plt.title("Diferencia (A - B)")
    elif operacion == "4":
        plt.title("Diferencia (B - A)")
    elif operacion == "5":
        plt.title("Diferencia simétrica (A Δ B)")
    plt.show()

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
        print("8. Mostrar diagrama de Venn")
        print("9. Salir")

        opcion = input("Elija una operación (1/2/3/4/5/6/7/8/9): ")
        match opcion:
            case "1":
                resultado = set1.union(set2)
                print("Unión:" if resultado else "Resultado: conjunto vacío.", resultado if resultado else "")
            case "2":
                resultado = set1.intersection(set2)
                print("Intersección:" if resultado else "No hay intersección (conjunto vacío).", resultado if resultado else "")
            case "3":
                resultado = set1.difference(set2)
                print("Diferencia (A - B):" if resultado else "Resultado: conjunto vacío.", resultado if resultado else "")
            case "4":
                resultado = set2.difference(set1)
                print("Diferencia (B - A):" if resultado else "Resultado: conjunto vacío.", resultado if resultado else "")
            case "5":
                resultado = set1.symmetric_difference(set2)
                print("Diferencia simétrica (A Δ B):" if resultado else "Resultado: conjunto vacío.", resultado if resultado else "")
            case "6":
                universo = obtener_universo()
                resultado = universo.difference(set1)
                print("Complemento de A:" if resultado else "El complemento de A es el conjunto vacío.", resultado if resultado else "")
            case "7":
                universo = obtener_universo()
                resultado = universo.difference(set2)
                print("Complemento de B:" if resultado else "El complemento de B es el conjunto vacío.", resultado if resultado else "")
            case "8":
                print("¿Qué operación desea visualizar en el diagrama de Venn?")
                print("1. Unión\n2. Intersección\n3. Diferencia (A - B)\n4. Diferencia (B - A)\n5. Diferencia simétrica (A Δ B)")
                op = input("Elija (1/2/3/4/5): ")
                if op in {"1", "2", "3", "4", "5"}:
                    mostrar_venn(set1, set2, op)
                else:
                    print("Opción inválida.")
            case "9":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")           
if __name__ == "__main__":
    main()