import tkinter as tk
from tkinter import ttk
from servicios.tarea_servicio import TareaServicio

class AppTkinter:
    def __init__(self, root, tarea_servicio):
        self.tarea_servicio = tarea_servicio
        self.root = root
        self.root.title("Lista de Tareas")

        # Frame principal
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Campo de entrada para nuevas tareas
        self.entry_tarea = ttk.Entry(main_frame, width=40)
        self.entry_tarea.grid(row=0, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        self.entry_tarea.bind("<Return>", self.agregar_tarea_event)

        # Botón Añadir Tarea
        btn_add = ttk.Button(main_frame, text="Añadir Tarea", command=self.agregar_tarea)
        btn_add.grid(row=0, column=1, padx=5, pady=5)

        # Treeview para mostrar las tareas
        self.tree = ttk.Treeview(main_frame, columns=("ID", "Descripción", "Estado"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Estado", text="Estado")
        self.tree.column("ID", width=50, anchor=tk.CENTER)
        self.tree.column("Descripción", width=300)
        self.tree.column("Estado", width=100, anchor=tk.CENTER)
        self.tree.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Scrollbar para el Treeview
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, column=2, sticky=(tk.N, tk.S))

        # Botones de acción
        btn_complete = ttk.Button(main_frame, text="Marcar Completada", command=self.completar_tarea)
        btn_complete.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        btn_delete = ttk.Button(main_frame, text="Eliminar", command=self.eliminar_tarea)
        btn_delete.grid(row=2, column=1, padx=5, pady=5, sticky=tk.E)

        # Evento de doble clic para completar tarea
        self.tree.bind("<Double-1>", self.completar_tarea_event)

        self.cargar_tareas()

    def cargar_tareas(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for tarea in self.tarea_servicio.listar_tareas():
            estado = "Completada" if tarea.estado_completado else "Pendiente"
            self.tree.insert("", tk.END, iid=tarea.id, values=(tarea.id, tarea.descripcion, estado))
            if tarea.estado_completado:
                self.tree.item(tarea.id, tags=("completed",))
        self.tree.tag_configure("completed", foreground="gray", font=("TkDefaultFont", 10, "overstrike"))

    def agregar_tarea(self):
        descripcion = self.entry_tarea.get()
        if descripcion:
            self.tarea_servicio.agregar_tarea(descripcion)
            self.entry_tarea.delete(0, tk.END)
            self.cargar_tareas()

    def agregar_tarea_event(self, event):
        self.agregar_tarea()

    def completar_tarea(self):
        selected_item = self.tree.focus()
        if selected_item:
            tarea_id = int(self.tree.item(selected_item)["values"][0])
            self.tarea_servicio.completar_tarea(tarea_id)
            self.cargar_tareas()

    def completar_tarea_event(self, event):
        self.completar_tarea()

    def eliminar_tarea(self):
        selected_item = self.tree.focus()
        if selected_item:
            tarea_id = int(self.tree.item(selected_item)["values"][0])
            self.tarea_servicio.eliminar_tarea(tarea_id)
            self.cargar_tareas()
