import tkinter as tk
from tkinter import ttk, messagebox

ARCHIVO = "ventas.txt"
RETIRA = "retira en el aserradero"
ENVIO = "envío a domicilio"


class AppVentas:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de ventas - Aserradero")
        self.root.resizable(False, False)

        # Variables ligadas a los campos del formulario
        self.var_tipo = tk.StringVar()
        self.var_precio = tk.StringVar()
        self.var_fecha = tk.StringVar()
        self.var_cliente = tk.StringVar()
        self.var_entrega = tk.StringVar(value=RETIRA)
        self.var_direccion = tk.StringVar()

        self.crear_formulario()
        self.crear_tabla()
        self.cargar_tabla()

    # ---------- Interfaz ----------
    def crear_formulario(self):
        marco = ttk.LabelFrame(self.root, text="Nueva venta", padding=10)
        marco.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(marco, text="Tipo de madera:").grid(row=0, column=0, sticky="w", pady=3)
        ttk.Entry(marco, textvariable=self.var_tipo, width=35).grid(row=0, column=1, pady=3)

        ttk.Label(marco, text="Precio ($):").grid(row=1, column=0, sticky="w", pady=3)
        ttk.Entry(marco, textvariable=self.var_precio, width=35).grid(row=1, column=1, pady=3)

        ttk.Label(marco, text="Fecha de la venta:").grid(row=2, column=0, sticky="w", pady=3)
        ttk.Entry(marco, textvariable=self.var_fecha, width=35).grid(row=2, column=1, pady=3)

        ttk.Label(marco, text="Cliente:").grid(row=3, column=0, sticky="w", pady=3)
        ttk.Entry(marco, textvariable=self.var_cliente, width=35).grid(row=3, column=1, pady=3)

        ttk.Label(marco, text="Método de entrega:").grid(row=4, column=0, sticky="w", pady=3)
        combo = ttk.Combobox(
            marco,
            textvariable=self.var_entrega,
            values=[RETIRA, ENVIO],
            state="readonly",
            width=32,
        )
        combo.grid(row=4, column=1, pady=3)
        combo.bind("<<ComboboxSelected>>", self.cambio_entrega)

        ttk.Label(marco, text="Dirección de envío:").grid(row=5, column=0, sticky="w", pady=3)
        self.entry_direccion = ttk.Entry(
            marco, textvariable=self.var_direccion, width=35, state="disabled"
        )
        self.entry_direccion.grid(row=5, column=1, pady=3)

        botones = ttk.Frame(marco)
        botones.grid(row=6, column=0, columnspan=2, pady=(10, 0))
        ttk.Button(botones, text="Guardar venta", command=self.guardar_venta).pack(side="left", padx=5)
        ttk.Button(botones, text="Limpiar", command=self.limpiar).pack(side="left", padx=5)
        ttk.Button(botones, text="Salir", command=self.root.destroy).pack(side="left", padx=5)

    def crear_tabla(self):
        marco = ttk.LabelFrame(self.root, text="Ventas registradas", padding=10)
        marco.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")

        columnas = ("tipo", "precio", "fecha", "cliente", "entrega", "direccion")
        encabezados = ("Tipo", "Precio", "Fecha", "Cliente", "Entrega", "Dirección")
        anchos = (100, 70, 80, 110, 150, 150)

        self.tabla = ttk.Treeview(marco, columns=columnas, show="headings", height=8)
        for col, texto, ancho in zip(columnas, encabezados, anchos):
            self.tabla.heading(col, text=texto)
            self.tabla.column(col, width=ancho)

        scroll = ttk.Scrollbar(marco, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)
        self.tabla.grid(row=0, column=0)
        scroll.grid(row=0, column=1, sticky="ns")

    # ---------- Lógica ----------
    def cambio_entrega(self, evento=None):
        """Habilita el campo de dirección solo si es envío a domicilio."""
        if self.var_entrega.get() == ENVIO:
            self.entry_direccion.config(state="normal")
        else:
            self.var_direccion.set("")
            self.entry_direccion.config(state="disabled")

    def limpiar(self):
        self.var_tipo.set("")
        self.var_precio.set("")
        self.var_fecha.set("")
        self.var_cliente.set("")
        self.var_entrega.set(RETIRA)
        self.cambio_entrega()

    def guardar_venta(self):
        tipo = self.var_tipo.get().strip()
        fecha = self.var_fecha.get().strip()
        cliente = self.var_cliente.get().strip()
        entrega = self.var_entrega.get()
        direccion = self.var_direccion.get().strip()

        # Validaciones
        if not tipo or not fecha or not cliente:
            messagebox.showwarning("Faltan datos", "Completá tipo, fecha y cliente.")
            return
        try:
            precio = int(self.var_precio.get())
        except ValueError:
            messagebox.showerror("Precio inválido", "El precio debe ser un número entero.")
            return
        if entrega == ENVIO and not direccion:
            messagebox.showwarning("Falta la dirección", "Ingresá la dirección de envío.")
            return

        # Misma estructura de línea que el programa original
        linea = f"{tipo}\t${precio}\t{fecha}\t{cliente}\t{entrega}\t{direccion}\n"

        try:
            with open(ARCHIVO, "a", encoding="utf-8") as archivo:
                archivo.write(linea)
        except PermissionError:
            messagebox.showerror("Error", "Error con los permisos.")
            return
        except OSError as error:
            messagebox.showerror("Error", f"Problema con el archivo usando el SO: {error}")
            return

        messagebox.showinfo("Listo", "Venta registrada correctamente.")
        self.limpiar()
        self.cargar_tabla()

    def cargar_tabla(self):
        """Lee ventas.txt y muestra su contenido en la tabla."""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    campos = linea.rstrip("\n").split("\t")
                    if len(campos) < 6:
                        campos += [""] * (6 - len(campos))
                    self.tabla.insert("", "end", values=campos[:6])
        except FileNotFoundError:
            pass  # todavía no hay ventas cargadas
        except OSError as error:
            messagebox.showerror("Error", f"No se pudo leer el archivo: {error}")


def main():
    root = tk.Tk()
    AppVentas(root)
    root.mainloop()


if __name__ == "__main__":
    main()
