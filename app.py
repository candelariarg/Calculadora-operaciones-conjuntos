"""
Punto de entrada principal. Permite elegir entre modo consola o interfaz gráfica.
"""

def menu():
    while True:
        print("Seleccione el modo de uso:")
        print("1. Modo consola")
        print("2. Modo interfaz gráfica (Tkinter)")
        opcion = input("Ingrese 1 o 2: ").strip()
        if opcion == "1":
            from consola import main_consola
            main_consola()
            break
        elif opcion == "2":
            from gui import crear_interfaz
            crear_interfaz()
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

if __name__ == "__main__":
    menu()
