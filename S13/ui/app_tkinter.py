import tkinter as tk
from tkinter import ttk, messagebox
from servicios.garaje_servicio import GarajeServicio

class AppGaraje(tk.Tk):
    """
    Clase principal de la interfaz gráfica utilizando Tkinter.
    """
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión de Garaje - MinWare")
        self.geometry("600x500")
        self.resizable(False, False)
        
        # Instancia del servicio para manejar la lógica
        self.servicio = GarajeServicio()
        
        # Configuración de la interfaz
        self._crear_componentes()

    def _crear_componentes(self):
        # Título principal
        lbl_titulo = tk.Label(self, text="Registro de Vehículos - Garaje", font=("Arial", 16, "bold"), pady=20)
        lbl_titulo.pack()

        # Frame para el formulario
        frame_form = tk.LabelFrame(self, text="Datos del Vehículo", padx=20, pady=20)
        frame_form.pack(padx=20, pady=10, fill="x")

        # Campos de entrada
        tk.Label(frame_form, text="Placa:").grid(row=0, column=0, sticky="w", pady=5)
        self.ent_placa = tk.Entry(frame_form, width=30)
        self.ent_placa.grid(row=0, column=1, pady=5)

        tk.Label(frame_form, text="Marca:").grid(row=1, column=0, sticky="w", pady=5)
        self.ent_marca = tk.Entry(frame_form, width=30)
        self.ent_marca.grid(row=1, column=1, pady=5)

        tk.Label(frame_form, text="Propietario:").grid(row=2, column=0, sticky="w", pady=5)
        self.ent_propietario = tk.Entry(frame_form, width=30)
        self.ent_propietario.grid(row=2, column=1, pady=5)

        # Botones de acción
        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=10)

        btn_agregar = tk.Button(frame_botones, text="Agregar Vehículo", command=self._agregar_vehiculo, bg="#4CAF50", fg="white", padx=10)
        btn_agregar.pack(side="left", padx=10)

        btn_limpiar = tk.Button(frame_botones, text="Limpiar Formulario", command=self._limpiar_formulario, bg="#f44336", fg="white", padx=10)
        btn_limpiar.pack(side="left", padx=10)

        # Tabla para visualizar vehículos
        self.tabla = ttk.Treeview(self, columns=("Placa", "Marca", "Propietario"), show="headings")
        self.tabla.heading("Placa", text="Placa")
        self.tabla.heading("Marca", text="Marca")
        self.tabla.heading("Propietario", text="Propietario")
        self.tabla.column("Placa", width=100, anchor="center")
        self.tabla.column("Marca", width=150, anchor="center")
        self.tabla.column("Propietario", width=200, anchor="center")
        self.tabla.pack(padx=20, pady=10, fill="both", expand=True)

        # Marca de agua en la base de la ventana
        lbl_marca_agua = tk.Label(self, text="Desarrollado por MINAYA GARCIA CRISTOPHER - Sistema de Gestión de Garaje v1.0", 
                                  font=("Arial", 8, "italic"), fg="BLUE", pady=5)
        lbl_marca_agua.pack(side="bottom")

    def _agregar_vehiculo(self):
        """
        Evento para el botón Agregar Vehículo.
        """
        placa = self.ent_placa.get().strip()
        marca = self.ent_marca.get().strip()
        propietario = self.ent_propietario.get().strip()

        try:
            # Llamada al servicio para registrar el vehículo
            self.servicio.agregar_vehiculo(placa, marca, propietario)
            
            # Actualizar la tabla
            self.tabla.insert("", "end", values=(placa, marca, propietario))
            
            # Limpiar campos y mostrar mensaje de éxito
            self._limpiar_formulario()
            messagebox.showinfo("Éxito", f"Vehículo con placa {placa} registrado correctamente.")
            
        except ValueError as e:
            messagebox.showwarning("Advertencia", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")

    def _limpiar_formulario(self):
        """
        Evento para el botón Limpiar Formulario.
        """
        self.ent_placa.delete(0, tk.END)
        self.ent_marca.delete(0, tk.END)
        self.ent_propietario.delete(0, tk.END)
        self.ent_placa.focus()
