import tkinter as tk #importamos libreria tkinter
from tkinter import messagebox, ttk

# Función para calcular la cuota
def calcular_cuota():
    try:
        # Obtener valores del formulario
        prestamo = float(entry_prestamo.get())
        tasa = float(entry_tasa.get()) / 100 / 12  # Tasa mensual
        meses = int(entry_meses.get())

        # Fórmula de cuota mensual
        if tasa == 0:  # Caso sin intereses
            cuota = prestamo / meses
        else:
            cuota = prestamo * (tasa * (1 + tasa) ** meses) / ((1 + tasa) ** meses - 1)

        # Mostrar resultado
        label_resultado.config(
            text=f"Cuota mensual: ${cuota:,.2f}",
            fg="green",
            font=("Arial", 12, "bold")
        )

        # Guardar para resumen
        global datos_credito
        datos_credito = (prestamo, tasa, meses, cuota)

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")


# Función para mostrar resumen y tabla en nueva ventana
def mostrar_resumen():
    try:
        prestamo, tasa, meses, cuota = datos_credito
    except:
        messagebox.showerror("Error", "Primero debes calcular la cuota.")
        return

    total_pagado = cuota * meses
    intereses_totales = total_pagado - prestamo

    # Crear ventana nueva
    resumen_win = tk.Toplevel(root)
    resumen_win.title("Resumen del Crédito")
    resumen_win.geometry("700x500")

    # Resumen general
    tk.Label(resumen_win, text=f"Préstamo solicitado: ${prestamo:,.2f}", font=("Arial", 11, "bold")).pack(anchor="w", padx=10, pady=5)
    tk.Label(resumen_win, text=f"Meses: {meses}", font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)
    tk.Label(resumen_win, text=f"Cuota mensual: ${cuota:,.2f}", font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)
    tk.Label(resumen_win, text=f"Total pagado: ${total_pagado:,.2f}", font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)
    tk.Label(resumen_win, text=f"Intereses totales: ${intereses_totales:,.2f}", font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)

    # Tabla de amortización
    cols = ("Mes", "Cuota", "Interés", "Abono Capital", "Saldo")
    tree = ttk.Treeview(resumen_win, columns=cols, show="headings", height=15)
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=120)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    saldo = prestamo
    for mes in range(1, meses + 1):
        interes = saldo * tasa
        abono_capital = cuota - interes
        saldo -= abono_capital
        tree.insert("", "end", values=(
            mes,
            f"${cuota:,.2f}",
            f"${interes:,.2f}",
            f"${abono_capital:,.2f}",
            f"${max(saldo,0):,.2f}"
        ))


# ---------------------- Ventana principal ----------------------
root = tk.Tk()
root.title("Simulador de Crédito - Libre Inversión")
root.geometry("420x300")
root.config(bg="#f4f4f4")

# Frame principal
frame = tk.Frame(root, bg="#f4f4f4", padx=20, pady=20)
frame.pack(expand=True)

# Campo: Valor del préstamo
tk.Label(frame, text="Valor del préstamo:", bg="#f4f4f4", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w")
entry_prestamo = tk.Entry(frame, width=20)
entry_prestamo.grid(row=0, column=1, pady=5)

# Campo: Tasa de interés anual
tk.Label(frame, text="Tasa de interés anual (%):", bg="#f4f4f4", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w")
entry_tasa = tk.Entry(frame, width=20)
entry_tasa.grid(row=1, column=1, pady=5)

# Campo: Meses
tk.Label(frame, text="Número de meses:", bg="#f4f4f4", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w")
entry_meses = tk.Entry(frame, width=20)
entry_meses.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Creado por Samir Vivas | 2025", bg="#f4f4f4", font=("Arial", 10, "bold")).grid(row=6, column=0, sticky="w")
tk.Label(frame, text="bryansamir@gmail.com", bg="#f4f4f4", font=("Arial", 10, "bold")).grid(row=7, column=0, sticky="w")

# Botón Calcular
btn_calcular = tk.Button(frame, text="Calcular cuota", command=calcular_cuota, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_calcular.grid(row=3, columnspan=2, pady=10)

# Botón Resumen
btn_resumen = tk.Button(frame, text="Ver Resumen", command=mostrar_resumen, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
btn_resumen.grid(row=4, columnspan=2, pady=10)

# Resultado
label_resultado = tk.Label(frame, text="", bg="#f4f4f4", font=("Arial", 10))
label_resultado.grid(row=5, columnspan=2, pady=10)

# Iniciar aplicación
root.mainloop()
