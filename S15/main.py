import tkinter as tk
from ui.app_tkinter import AppTkinter
from servicios.tarea_servicio import TareaServicio

if __name__ == "__main__":
    root = tk.Tk()
    tarea_servicio = TareaServicio()
    app = AppTkinter(root, tarea_servicio)
    root.mainloop()
