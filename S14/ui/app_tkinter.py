import tkinter as tk
from tkinter import ttk, messagebox

class AppVisitas(tk.Tk):
    def __init__(self, servicio):
        super().__init__()
        self.title("Sistema de Registro de Visitantes - Oficina - MinWare")
        self.geometry("750x600")
        self.resizable(False, False)
        
        # Inyección de Dependencias: El servicio se recibe como parámetro
        self.servicio = servicio
        
        # Configuración de la interfaz
        self._crear_componentes()

    def _crear_componentes(self):
        # Título principal
        lbl_titulo = tk.Label(self, text="Registro de Visitantes", font=("Arial", 18, "bold"), pady=20)
        lbl_titulo.pack()

        # Frame para el formulario de entrada
        frame_form = tk.LabelFrame(self, text="Datos del Visitante", padx=20, pady=20)
        frame_form.pack(padx=20, pady=10, fill="x")

        # Campos de entrada (Entry)
        tk.Label(frame_form, text="Cédula:").grid(row=0, column=0, sticky="w", pady=5)
        self.ent_cedula = tk.Entry(frame_form, width=35)
        self.ent_cedula.grid(row=0, column=1, pady=5)

        tk.Label(frame_form, text="Nombre Completo:").grid(row=1, column=0, sticky="w", pady=5)
        self.ent_nombre = tk.Entry(frame_form, width=35)
        self.ent_nombre.grid(row=1, column=1, pady=5)

        tk.Label(frame_form, text="Motivo de Visita:").grid(row=2, column=0, sticky="w", pady=5)
        self.ent_motivo = tk.Entry(frame_form, width=35)
        self.ent_motivo.grid(row=2, column=1, pady=5)

        # Panel de Acciones (Botones)
        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=15)

        btn_registrar = tk.Button(frame_botones, text="Registrar Visitante", command=self._registrar_visitante, 
                                  bg="#4CAF50", fg="white", padx=15, font=("Arial", 10, "bold"))
        btn_registrar.pack(side="left", padx=10)

        btn_eliminar = tk.Button(frame_botones, text="Eliminar Seleccionado", command=self._eliminar_visitante, 
                                 bg="#f44336", fg="white", padx=15, font=("Arial", 10, "bold"))
        btn_eliminar.pack(side="left", padx=10)

        btn_limpiar = tk.Button(frame_botones, text="Limpiar Campos", command=self._limpiar_campos, 
                                bg="#2196F3", fg="white", padx=15, font=("Arial", 10, "bold"))
        btn_limpiar.pack(side="left", padx=10)

        # Visualización de Datos (Tabla ttk.Treeview)
        self.tabla = ttk.Treeview(self, columns=("Cedula", "Nombre", "Motivo"), show="headings")
        self.tabla.heading("Cedula", text="Cédula")
        self.tabla.heading("Nombre", text="Nombre Completo")
        self.tabla.heading("Motivo", text="Motivo de Visita")
        self.tabla.column("Cedula", width=120, anchor="center")
        self.tabla.column("Nombre", width=200, anchor="w")
        self.tabla.column("Motivo", width=250, anchor="w")
        self.tabla.pack(padx=20, pady=10, fill="both", expand=True)

        # Marca de agua
        lbl_marca_agua = tk.Label(self, text="Desarrollado por MinWare - Sistema de Gestión de Visitas", 
                                  font=("Arial", 8, "italic"), fg="gray", pady=5)
        lbl_marca_agua.pack(side="bottom")

    def _registrar_visitante(self):
        cedula = self.ent_cedula.get().strip()
        nombre = self.ent_nombre.get().strip()
        motivo = self.ent_motivo.get().strip()

        try:
            # Llamada al servicio para registrar el visitante
            self.servicio.registrar_visitante(cedula, nombre, motivo)
            
            # Actualizar la tabla visualmente
            self.tabla.insert("", "end", values=(cedula, nombre, motivo))
            
            # Limpiar campos y mostrar mensaje de éxito
            self._limpiar_campos()
            messagebox.showinfo("Éxito", f"Visitante {nombre} registrado correctamente.")
            
        except ValueError as e:
            messagebox.showwarning("Advertencia", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")

    def _eliminar_visitante(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un visitante de la tabla para eliminar.")
            return
        
        # Obtener la cédula del elemento seleccionado en la tabla
        item = self.tabla.item(seleccion)
        cedula = item['values'][0]
        nombre = item['values'][1]
        
        confirmar = messagebox.askyesno("Confirmar", f"¿Está seguro de que desea eliminar a {nombre}?")
        if confirmar:
            if self.servicio.eliminar_visitante(cedula):
                self.tabla.delete(seleccion)
                messagebox.showinfo("Éxito", "Registro eliminado correctamente.")
            else:
                messagebox.showerror("Error", "No se pudo eliminar el registro del servicio.")

    def _limpiar_campos(self):
        self.ent_cedula.delete(0, tk.END)
        self.ent_nombre.delete(0, tk.END)
        self.ent_motivo.delete(0, tk.END)
        self.ent_cedula.focus()
