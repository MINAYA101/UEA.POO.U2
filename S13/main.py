import sys
import os

# Asegurar que el directorio raíz del proyecto esté en el path de Python
# para permitir importaciones relativas de los módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.app_tkinter import AppGaraje

def main():
    """
    Punto de entrada principal de la aplicación.
    """
    try:
        # Crear una instancia de la aplicación Tkinter
        app = AppGaraje()
        
        # Iniciar el bucle principal de eventos
        app.mainloop()
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")

if __name__ == "__main__":
    main()
