import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.app_tkinter import AppVisitas
from servicios.visita_servicio import VisitaServicio

def main():
    try:
        # 1. Crear la instancia del servicio (Capa de Lógica)
        servicio = VisitaServicio()
        
        # 2. Crear la instancia de la aplicación (Capa UI)
        # Se aplica Inyección de Dependencias pasando el servicio al constructor
        app = AppVisitas(servicio)
        
        # 3. Iniciar el bucle principal de eventos
        app.mainloop()
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")

if __name__ == "__main__":
    main()
