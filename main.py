from coches import coches
from tkinter import Label,Entry,Button,Tk,messagebox


class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestión de Coches")
        self.ventana.geometry("600x700")
        self.ventana.resizable(0,0)
        self.main()
   
    ##.  ... Vistas de Coches ....
    def borrarPantalla(self):
      for widget in self.ventana.winfo_children():
          widget.destroy()
    
    def menu_acciones(self):
        self.borrarPantalla()
        tipo="Coches"
        Label(self.ventana,text=f"\n...::: Menu de {tipo} :::... \n").pack(pady=10)
        Button(self.ventana,text="1.- Agregar",command=self.insertar_view).pack(pady=5)
        Button(self.ventana,text="2.- Borrar",command=self.eliminar_view).pack(pady=5)
        Button(self.ventana,text="3.- Modificar",command=self.modificar_view).pack(pady=5)
        Button(self.ventana,text="4.- Mostrar",command=self.consultar_view).pack(pady=5)
        Button(self.ventana,text="5.- Regresar",command=self.main).pack(pady=5)
        
    def main(self):
            self.borrarPantalla() 
            Label(self.ventana,text="\n...::: M E N U   P R I N C I P A L :::...").pack(pady=10)    
            Button(self.ventana,text="1.- Coches",command=self.menu_acciones).pack(pady=5) 
            Button(self.ventana,text="2.- Salir",command=self.ventana.quit).pack(pady=5)  
    
    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingresar los datos del Coche...").pack(pady=10)
        
        Label(self.ventana,text="Marca: ").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)
        
        Label(self.ventana,text="Color: ").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)
        
        Label(self.ventana,text="Modelo: ").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)
        
        Label(self.ventana,text="Velocidad: ").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)
        
        Label(self.ventana,text="Potencia: ").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)
        
        Label(self.ventana,text="# de Asientos: ").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)
        
        Button(self.ventana,text="Guardar",command=lambda:{self.insertar_controller(),self.insertar_view()}).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)
        
    def eliminar_view(self):
            self.borrarPantalla()
            Label(self.ventana,text="...Ingresar el ID del Coche a Eliminar...").pack(pady=10)
            
            Label(self.ventana,text="ID: ").pack(pady=5)
            self.id=Entry(self.ventana)
            self.id.focus()
            self.id.pack(pady=5)
            
            self.btn_buscar=Button(self.ventana,text="Buscar",command=lambda:self.buscar_controller("eliminar"))
            self.btn_buscar.pack(pady=5)
    
            self.btn_eliminar=Button(self.ventana,text="Eliminar",state="disabled",command=lambda:{self.eliminar_controller(),self.eliminar_view()})
            self.btn_eliminar.pack(pady=5)
            
            Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)
        
    def modificar_view(self):
       self.borrarPantalla()
       Label(self.ventana,text="...Ingresar el ID del Coche a modificar...").pack(pady=10)
                   
       Label(self.ventana,text="ID: ").pack(pady=5)
       self.id=Entry(self.ventana)
       self.id.focus()
       self.id.pack(pady=5)

       Label(self.ventana,text="Nueva Marca: ").pack(pady=5)
       self.marca=Entry(self.ventana)
       self.marca.pack(pady=5)
        
       Label(self.ventana,text=" Nuevo Color: ").pack(pady=5)
       self.color=Entry(self.ventana)
       self.color.pack(pady=5)
        
       Label(self.ventana,text="Nuevo Modelo: ").pack(pady=5)
       self.modelo=Entry(self.ventana)
       self.modelo.pack(pady=5)
        
       Label(self.ventana,text="Nueva Velocidad: ").pack(pady=5)
       self.velocidad=Entry(self.ventana)
       self.velocidad.pack(pady=5)
        
       Label(self.ventana,text="Nueva Potencia: ").pack(pady=5)
       self.potencia=Entry(self.ventana)
       self.potencia.pack(pady=5)
        
       Label(self.ventana,text="Nuevo # de Asientos: ").pack(pady=5)
       self.asientos=Entry(self.ventana)
       self.asientos.pack(pady=5)
        
       Button(self.ventana,text="Guardar",command=lambda:{self.modificar_controller(),self.modificar_view()}).pack(pady=10)
       Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)
       
    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text=" ::: Consultar los Coches :::").pack(pady=10)
        filas=""  
        filas=self.consultar_controller(filas)
        Label(self.ventana,text=f"{'No.':<15}{'ID':<15}{'Marca':<15} {'Color':<15}{'Modelo':<15}{'Velocidad':<15}{'Potencia':<15}{'# Asientos':<15}").pack(pady=5)
        Label(self.ventana,text=f"-"*100).pack(pady=5)
        Label(self.ventana,text=f"{filas}").pack(pady=5)
        Label(self.ventana,text=f"-"*100).pack(pady=5)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)

    def cambiar_estado_btn(self,estado,tipo_accion):
        if estado:
            if tipo_accion=="eliminar":
               self.btn_eliminar.config(state="normal")
            elif tipo_accion=="modificar": 
               self.btn_modificar.config(state="normal") 
        else:
            if tipo_accion=="eliminar":
               self.btn_eliminar.config(state="disabled")
            elif tipo_accion=="modificar":
               self.btn_modificar.config(state="disabled")   
    
    def confirmacion_eliminar(self,tipo):
        resp=messagebox.askquestion(title="...¡Atencion!...",message=f"...¿Desea {tipo} este registro?...")
        if resp=="yes":
           return True
        else:
            return False
    # ... Contralador de Coches ...
    def respuesta_sql(self,respuesta):
            if respuesta:
                messagebox.showinfo(title="... Exitoso ...",message="...¡Accion Realizada con Exito!...")
            else:
                messagebox.showerror(title="...¡ Verifica por favor !...",message="...¡Esta Accion no pudo realizarse en este momento!...")
       
    def insertar_controller(self):
        coche1=coches.Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta=coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1                 
    
    def eliminar_controller(self):
        id=self.id.get()
        resp=self.confirmacion_eliminar("eliminar")
        if resp:
           respuesta=coches.Coches.eliminar(id)
        else:
            respuesta=False   
        self.respuesta_sql(respuesta)
  
    def consultar_controller(self,filas):
       registros=coches.Coches.consultar()
       if len(registros)>0:
            num_coches=1
            for fila in registros:
                filas=filas+f"\n{num_coches:<15}{fila[0]:<15}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}{fila[6]:<15}"
                num_coches+=1
       else:
           filas="... ¡No existen datos que mostrar por el momento ...!"
       return filas   
           
    def modificar_controller(self):
        id=self.id.get()
        coche1=coches.Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta=coche1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche1        

    def buscar_controller(self,tipo_accion):
        id=self.id.get()
        coche1=coches.Coches.buscar(id)
        if len(coche1)>0: 
            messagebox.showinfo(title="...¡ Registro Encontrado !...",message=f"...¡El registro fue encontrado con exito, puedes {tipo_accion}!...")
            self.cambiar_estado_btn(True,tipo_accion) 
            # if tipo_accion=="modificar":
                # self.var_marca.set(coche1[0][1])
                # self.var_color.set(coche1[0][2])
                # self.var_modelo.set(coche1[0][3])
                # self.var_velocidad.set(coche1[0][4])
                # self.var_potencia.set(coche1[0][5])
                # self.var_asientos.set(coche1[0][6])
        else:
            messagebox.showerror(title="...¡ Verifica por favor !...",message=f"...¡El registro no fue encontrado, no es posible {tipo_accion}!...")
            self.cambiar_estado_btn(False,tipo_accion)  
            
if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()