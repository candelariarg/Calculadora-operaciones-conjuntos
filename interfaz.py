import tkinter as tk
from tkinter import ttk, messagebox
import re

def validar_entrada(texto):
    """Valida que la entrada sean solo elementos separados por comas (números o letras)."""
    patron = r"^\s*([\w]+\s*,\s*)*[\w]+\s*$|^\s*$"
    return re.match(patron, texto)

def texto_a_conjunto(texto):
    """Convierte una cadena de elementos separados por comas a un conjunto de strings."""
    return set(x.strip() for x in texto.split(",") if x.strip() != "")

def mostrar_resultado(resultado, etiqueta):
    etiqueta.config(text=f"Resultado: {{ {', '.join(sorted(resultado))} }}")

def operacion_union(entry_a, entry_b, etiqueta):
    a = entry_a.get()
    b = entry_b.get()
    if not (validar_entrada(a) and validar_entrada(b)):
        messagebox.showerror("Error de entrada", "Ingrese elementos separados por comas (números o letras).")
        return
    conjunto_a = texto_a_conjunto(a)
    conjunto_b = texto_a_conjunto(b)
    mostrar_resultado(conjunto_a | conjunto_b, etiqueta)

def operacion_interseccion(entry_a, entry_b, etiqueta):
    a = entry_a.get()
    b = entry_b.get()
    if not (validar_entrada(a) and validar_entrada(b)):
        messagebox.showerror("Error de entrada", "Ingrese elementos separados por comas (números o letras).")
        return
    conjunto_a = texto_a_conjunto(a)
    conjunto_b = texto_a_conjunto(b)
    mostrar_resultado(conjunto_a & conjunto_b, etiqueta)

def operacion_diferencia(entry_a, entry_b, etiqueta):
    a = entry_a.get()
    b = entry_b.get()
    if not (validar_entrada(a) and validar_entrada(b)):
        messagebox.showerror("Error de entrada", "Ingrese elementos separados por comas (números o letras).")
        return
    conjunto_a = texto_a_conjunto(a)
    conjunto_b = texto_a_conjunto(b)
    mostrar_resultado(conjunto_a - conjunto_b, etiqueta)

def operacion_diferencia_ba(entry_a, entry_b, etiqueta):
    a = entry_a.get()
    b = entry_b.get()
    if not (validar_entrada(a) and validar_entrada(b)):
        messagebox.showerror("Error de entrada", "Ingrese elementos separados por comas (números o letras).")
        return
    conjunto_a = texto_a_conjunto(a)
    conjunto_b = texto_a_conjunto(b)
    mostrar_resultado(conjunto_b - conjunto_a, etiqueta)

def operacion_diferencia_simetrica(entry_a, entry_b, etiqueta):
    a = entry_a.get()
    b = entry_b.get()
    if not (validar_entrada(a) and validar_entrada(b)):
        messagebox.showerror("Error de entrada", "Ingrese elementos separados por comas (números o letras).")
        return
    conjunto_a = texto_a_conjunto(a)
    conjunto_b = texto_a_conjunto(b)
    mostrar_resultado(conjunto_a ^ conjunto_b, etiqueta)

def operacion_complemento_a(entry_a, entry_b, etiqueta):
    a = entry_a.get()
    b = entry_b.get()
    if not (validar_entrada(a) and validar_entrada(b)):
        messagebox.showerror("Error de entrada", "Ingrese elementos separados por comas (números o letras).")
        return
    conjunto_a = texto_a_conjunto(a)
    conjunto_b = texto_a_conjunto(b)
    universo = conjunto_a | conjunto_b
    mostrar_resultado(universo - conjunto_a, etiqueta)

def operacion_complemento_b(entry_a, entry_b, etiqueta):
    a = entry_a.get()
    b = entry_b.get()
    if not (validar_entrada(a) and validar_entrada(b)):
        messagebox.showerror("Error de entrada", "Ingrese elementos separados por comas (números o letras).")
        return
    conjunto_a = texto_a_conjunto(a)
    conjunto_b = texto_a_conjunto(b)
    universo = conjunto_a | conjunto_b
    mostrar_resultado(universo - conjunto_b, etiqueta)

def limpiar_entry(entry):
    entry.delete(0, tk.END)

def crear_interfaz():
    root = tk.Tk()
    root.title("Operaciones entre Conjuntos")
    root.configure(bg="#f4f8fb")
    root.minsize(600, 420)

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton', font=('Segoe UI', 13), padding=10, background="#4a90e2", foreground="#fff")
    style.map('TButton', background=[('active', '#357ab8')])
    style.configure('TLabel', font=('Segoe UI', 13), background="#f4f8fb", foreground="#222")
    style.configure('Result.TLabel', font=('Segoe UI', 14, 'bold'), foreground="#357ab8", background="#f4f8fb")
    style.configure('Clear.TButton', font=('Segoe UI', 10), padding=2, background="#e74c3c", foreground="#fff")
    style.map('Clear.TButton', background=[('active', '#c0392b')])

    main_frame = ttk.Frame(root, padding=30, style='TFrame')
    main_frame.pack(fill='both', expand=True)
    main_frame.columnconfigure(1, weight=1)

    # Conjunto A
    label_a = ttk.Label(main_frame, text="Conjunto A:")
    label_a.grid(row=0, column=0, sticky='w', pady=(0,10))
    entry_a = ttk.Entry(main_frame, font=('Segoe UI', 13))
    entry_a.grid(row=0, column=1, sticky='ew', pady=(0,10), ipady=5)
    clear_a = ttk.Button(main_frame, text="✖", width=2, style='Clear.TButton', command=lambda: limpiar_entry(entry_a))
    clear_a.grid(row=0, column=2, sticky='w', padx=(8,0), pady=(0,10))

    # Conjunto B
    label_b = ttk.Label(main_frame, text="Conjunto B:")
    label_b.grid(row=1, column=0, sticky='w', pady=(0,20))
    entry_b = ttk.Entry(main_frame, font=('Segoe UI', 13))
    entry_b.grid(row=1, column=1, sticky='ew', pady=(0,20), ipady=5)
    clear_b = ttk.Button(main_frame, text="✖", width=2, style='Clear.TButton', command=lambda: limpiar_entry(entry_b))
    clear_b.grid(row=1, column=2, sticky='w', padx=(8,0), pady=(0,20))

    # Botones de operaciones
    botones = [
        ("Unión (A ∪ B)", lambda: operacion_union(entry_a, entry_b, resultado_label)),
        ("Intersección (A ∩ B)", lambda: operacion_interseccion(entry_a, entry_b, resultado_label)),
        ("Diferencia (A - B)", lambda: operacion_diferencia(entry_a, entry_b, resultado_label)),
        ("Diferencia (B - A)", lambda: operacion_diferencia_ba(entry_a, entry_b, resultado_label)),
        ("Diferencia simétrica (A Δ B)", lambda: operacion_diferencia_simetrica(entry_a, entry_b, resultado_label)),
        ("Complemento de A", lambda: operacion_complemento_a(entry_a, entry_b, resultado_label)),
        ("Complemento de B", lambda: operacion_complemento_b(entry_a, entry_b, resultado_label)),
        ("Salir", root.destroy)
    ]
    botones_frame = ttk.Frame(main_frame)
    botones_frame.grid(row=2, column=0, columnspan=3, pady=(0,20), sticky='ew')
    for i, (texto, comando) in enumerate(botones):
        btn = ttk.Button(botones_frame, text=texto, command=comando, style='TButton')
        btn.grid(row=i//2, column=i%2, padx=12, pady=8, sticky='ew')
        botones_frame.columnconfigure(i%2, weight=1)

    # Resultado
    resultado_label = ttk.Label(main_frame, text="Resultado: ", style='Result.TLabel', anchor='center')
    resultado_label.grid(row=3, column=0, columnspan=3, pady=(10,0), sticky='ew')

    # Responsive
    for i in range(3):
        main_frame.columnconfigure(i, weight=1)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    root.mainloop()

if __name__ == "__main__":
    crear_interfaz()
