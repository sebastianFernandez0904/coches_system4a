# from tkinter import *
# from tkinter import ttk, messagebox
# from coches import cochesBD


# class App:
#     CAMPOS = ["Marca", "Color", "Modelo", "Velocidad", "Potencia", "Asientos"]

#     def __init__(self, ventana):
#         self.ventana = ventana
#         self.ventana.title("Gestion de Coches")
#         self.ventana.geometry("600x800")
#         self.ventana.resizable(0, 0)

#         # Todas las vistas se dibujan dentro de este contenedor
#         self.contenedor = Frame(self.ventana)
#         self.contenedor.pack(fill=BOTH, expand=True)
#         self.vistaMenu()

#     # ---------- utilidades ----------
#     def limpiar(self):
#         for widget in self.contenedor.winfo_children():
#             widget.destroy()

#     def titulo(self, texto):
#         Label(self.contenedor, text=texto, font=("Arial", 18, "bold")).pack(pady=20)

#     def botonRegresar(self):
#         Button(self.contenedor, text="Regresar", width=20,
#                command=self.vistaMenu).pack(pady=10)

#     def crearCampos(self):
#         """Crea los Entry del formulario y los regresa en un diccionario."""
#         entradas = {}
#         for campo in self.CAMPOS:
#             fila = Frame(self.contenedor)
#             fila.pack(pady=5)
#             Label(fila, text=f"{campo}:", width=12, anchor="e").pack(side=LEFT)
#             entrada = Entry(fila, width=30)
#             entrada.pack(side=LEFT)
#             entradas[campo] = entrada
#         return entradas

#     def leerDatos(self, entradas):
#         """Valida y regresa los datos; si hay error regresa None."""
#         marca = entradas["Marca"].get().upper().strip()
#         color = entradas["Color"].get().upper().strip()
#         modelo = entradas["Modelo"].get().upper().strip()
#         velocidad = entradas["Velocidad"].get().strip()
#         potencia = entradas["Potencia"].get().strip()
#         asientos = entradas["Asientos"].get().strip()

#         if not all([marca, color, modelo, velocidad, potencia, asientos]):
#             messagebox.showwarning("Datos incompletos", "Llena todos los campos.")
#             return None
#         if not (velocidad.isdigit() and potencia.isdigit() and asientos.isdigit()):
#             messagebox.showwarning("Datos inválidos",
#                                    "Velocidad, potencia y asientos deben ser números.")
#             return None
#         return marca, color, modelo, velocidad, potencia, asientos

#     def respuestaSql(self, respuesta):
#         if respuesta:
#             messagebox.showinfo("Éxito", "¡Acción realizada con éxito!")
#         else:
#             messagebox.showerror("Error", "¡No se pudo realizar la acción!")

#     # ---------- vistas ----------
#     def vistaMenu(self):
#         self.limpiar()
#         self.titulo("M E N Ú   P R I N C I P A L")
#         opciones = [
#             ("Agregar", self.vistaAgregar),
#             ("Borrar", self.vistaBorrar),
#             ("Modificar", self.vistaModificar),
#             ("Mostrar", self.vistaMostrar),
#             ("Salir", self.ventana.destroy),
#         ]
#         for texto, comando in opciones:
#             Button(self.contenedor, text=texto, width=25, height=2,
#                    command=comando).pack(pady=10)

#     def vistaAgregar(self):
#         self.limpiar()
#         self.titulo("Agregar coche")
#         entradas = self.crearCampos()

#         def guardar():
#             datos = self.leerDatos(entradas)
#             if datos is None:
#                 return
#             coche = cochesBD.CochesBD(*datos)
#             self.respuestaSql(coche.insertar())
#             for e in entradas.values():
#                 e.delete(0, END)

#         Button(self.contenedor, text="Guardar", width=20, command=guardar).pack(pady=15)
#         self.botonRegresar()

#     def vistaBorrar(self):
#         self.limpiar()
#         self.titulo("Borrar coche")
#         fila = Frame(self.contenedor)
#         fila.pack(pady=5)
#         Label(fila, text="ID:", width=12, anchor="e").pack(side=LEFT)
#         entradaId = Entry(fila, width=30)
#         entradaId.pack(side=LEFT)

#         def borrar():
#             id = entradaId.get().strip()
#             if not id.isdigit():
#                 messagebox.showwarning("ID inválido", "Escribe un ID numérico.")
#                 return
#             if not messagebox.askyesno("Confirmar", f"¿Eliminar el coche con ID {id}?"):
#                 return
#             coche = cochesBD.CochesBD('', '', '', 0, 0, 0)
#             self.respuestaSql(coche.eliminar(id))
#             entradaId.delete(0, END)

#         Button(self.contenedor, text="Borrar", width=20, command=borrar).pack(pady=15)
#         self.botonRegresar()

#     def vistaModificar(self):
#         self.limpiar()
#         self.titulo("Modificar coche")

#         fila = Frame(self.contenedor)
#         fila.pack(pady=5)
#         Label(fila, text="ID:", width=12, anchor="e").pack(side=LEFT)
#         entradaId = Entry(fila, width=20)
#         entradaId.pack(side=LEFT)

#         entradas = self.crearCampos()

#         def buscar():
#             id = entradaId.get().strip()
#             if not id.isdigit():
#                 messagebox.showwarning("ID inválido", "Escribe un ID numérico.")
#                 return
#             coche = cochesBD.CochesBD('', '', '', 0, 0, 0)
#             for reg in coche.consultar():
#                 if str(reg[0]) == id:
#                     for campo, valor in zip(self.CAMPOS, reg[1:]):
#                         entradas[campo].delete(0, END)
#                         entradas[campo].insert(0, valor)
#                     return
#             messagebox.showinfo("Sin resultados", "No existe un coche con ese ID.")

#         Button(fila, text="Buscar", command=buscar).pack(side=LEFT, padx=5)

#         def actualizar():
#             id = entradaId.get().strip()
#             if not id.isdigit():
#                 messagebox.showwarning("ID inválido", "Escribe un ID numérico.")
#                 return
#             datos = self.leerDatos(entradas)
#             if datos is None:
#                 return
#             coche = cochesBD.CochesBD(*datos)
#             self.respuestaSql(coche.actualizar(id))

#         Button(self.contenedor, text="Actualizar", width=20, command=actualizar).pack(pady=15)
#         self.botonRegresar()

#     def vistaMostrar(self):
#         self.limpiar()
#         self.titulo("Lista de coches")

#         columnas = ["ID"] + self.CAMPOS
#         tabla = ttk.Treeview(self.contenedor, columns=columnas, show="headings", height=20)
#         for col in columnas:
#             tabla.heading(col, text=col)
#             tabla.column(col, width=60 if col == "ID" else 85, anchor="center")
#         tabla.pack(padx=10, pady=10, fill=X)

#         coche = cochesBD.CochesBD('', '', '', 0, 0, 0)
#         registros = coche.consultar()
#         if registros:
#             for fila in registros:
#                 tabla.insert("", END, values=fila)
#         else:
#             Label(self.contenedor, text="¡Por el momento no hay datos que mostrar!").pack()

#         self.botonRegresar()


# if __name__ == "__main__":
#     ventana = Tk()
#     app = App(ventana)
#     ventana.mainloop()

from tkinter import *
from tkinter import messagebox
from coches import coches


class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de Coches")
        self.ventana.geometry("500x550")
        self.main()

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo("Aviso", "Accion Realizada con Exito")
        else:
            messagebox.showerror("Aviso", "Esta Accion no pudo realizarse")

    def crear_campo(self, texto):
        Label(self.ventana, text=texto).pack()
        entrada = Entry(self.ventana)
        entrada.pack()
        return entrada

    def crear_campos_coche(self):
        self.marca = self.crear_campo("Marca")
        self.color = self.crear_campo("Color")
        self.modelo = self.crear_campo("Modelo")
        self.velocidad = self.crear_campo("Velocidad")
        self.potencia = self.crear_campo("Potencia")
        self.asientos = self.crear_campo("Asientos")

    def leer_datos_coche(self):
        marca = self.marca.get().strip()
        color = self.color.get().strip()
        modelo = self.modelo.get().strip()
        if not marca or not color or not modelo:
            raise ValueError("Campos vacios")
        velocidad = int(self.velocidad.get().strip())
        potencia = int(self.potencia.get().strip())
        asientos = int(self.asientos.get().strip())
        return coches.Coches(marca, color, modelo, velocidad, potencia, asientos)

    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Ingresar datos del coche").pack(pady=5)
        self.crear_campos_coche()
        Button(self.ventana, text="Guardar", command=self.guardar_coche).pack(pady=5)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=5)

    def guardar_coche(self):
        try:
            coche = self.leer_datos_coche()
        except ValueError:
            messagebox.showerror("Error", "Datos invalidos")
            return
        respuesta = coche.insertar()
        self.respuesta_sql(respuesta)
        self.menu_acciones()

    def eliminar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Ingresar el ID del coche a borrar").pack(pady=5)
        self.id_eliminar = self.crear_campo("ID")
        Button(self.ventana, text="Eliminar", command=self.procesar_eliminacion).pack(pady=5)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=5)

    def procesar_eliminacion(self):
        try:
            id_coche = int(self.id_eliminar.get().strip())
        except ValueError:
            messagebox.showerror("Error", "ID invalido")
            return
        respuesta = coches.Coches.eliminar(id_coche)
        self.respuesta_sql(respuesta)
        self.menu_acciones()

    def modificar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Ingresar ID y datos nuevos").pack(pady=5)
        self.id_modificar = self.crear_campo("ID del Coche")
        self.crear_campos_coche()
        Button(self.ventana, text="Actualizar", command=self.procesar_modificacion).pack(pady=5)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=5)

    def procesar_modificacion(self):
        try:
            id_coche = int(self.id_modificar.get().strip())
            coche = self.leer_datos_coche()
        except ValueError:
            messagebox.showerror("Error", "Datos invalidos")
            return
        respuesta = coche.actualizar(id_coche)
        self.respuesta_sql(respuesta)
        self.menu_acciones()

    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Listado de Coches").pack(pady=5)

        texto = Text(self.ventana, width=55, height=18)
        texto.pack(pady=5)

        registros = coches.Coches.consultar()
        if registros:
            for fila in registros:
                linea = (f"ID: {fila[0]} | Marca: {fila[1]} | Color: {fila[2]} | "
                         f"Modelo: {fila[3]} | Vel: {fila[4]} | Pot: {fila[5]} | "
                         f"Asientos: {fila[6]}\n")
                texto.insert(END, linea)
        else:
            texto.insert(END, "No existen datos que mostrar.")

        texto.config(state=DISABLED)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=5)

    def menu_acciones(self):
        self.borrarPantalla()
        Label(self.ventana, text="Menu de Coches").pack(pady=10)
        Button(self.ventana, text="1.- Agregar", command=self.insertar_view).pack(pady=2)
        Button(self.ventana, text="2.- Borrar", command=self.eliminar_view).pack(pady=2)
        Button(self.ventana, text="3.- Modificar", command=self.modificar_view).pack(pady=2)
        Button(self.ventana, text="4.- Mostrar", command=self.consultar_view).pack(pady=2)
        Button(self.ventana, text="5.- Regresar", command=self.main).pack(pady=2)

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text="MENU PRINCIPAL").pack(pady=20)
        Button(self.ventana, text="1.- Coches", command=self.menu_acciones).pack(pady=5)
        Button(self.ventana, text="2.- Salir", command=self.ventana.destroy).pack(pady=5)


if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()