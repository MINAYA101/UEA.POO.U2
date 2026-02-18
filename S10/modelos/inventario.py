import os
from modelos.producto import Producto

class Inventario:
    """
    Gestiona la colección de productos y su persistencia en un archivo de texto.
    """
    def __init__(self, archivo_datos="inventario.txt"):
        self.archivo_datos = archivo_datos
        self.productos = {}
        self._cargar_desde_archivo()

    def _cargar_desde_archivo(self):
        """Carga los productos desde el archivo al iniciar el programa."""
        if not os.path.exists(self.archivo_datos):
            # Si el archivo no existe, lo creamos vacío
            try:
                with open(self.archivo_datos, 'w', encoding='utf-8') as f:
                    pass
                print(f"[INFO] Archivo '{self.archivo_datos}' creado exitosamente.")
            except (PermissionError, IOError) as e:
                print(f"[ERROR] No se pudo crear el archivo de inventario: {e}")
            return

        try:
            with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                for linea in f:
                    producto = Producto.from_line(linea)
                    if producto:
                        self.productos[producto.id_producto] = producto
            print(f"[INFO] Se cargaron {len(self.productos)} productos desde el archivo.")
        except FileNotFoundError:
            print(f"[ERROR] El archivo '{self.archivo_datos}' no fue encontrado.")
        except PermissionError:
            print(f"[ERROR] Permisos insuficientes para leer '{self.archivo_datos}'.")
        except Exception as e:
            print(f"[ERROR] Error inesperado al cargar datos: {e}")

    def _guardar_en_archivo(self):
        """Guarda el estado actual del inventario en el archivo."""
        try:
            with open(self.archivo_datos, 'w', encoding='utf-8') as f:
                for producto in self.productos.values():
                    f.write(producto.to_line())
            return True
        except PermissionError:
            print(f"[ERROR] No tienes permisos para escribir en '{self.archivo_datos}'.")
            return False
        except Exception as e:
            print(f"[ERROR] Error al guardar en el archivo: {e}")
            return False

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            return False, "El ID ya existe en el inventario."
        
        self.productos[producto.id_producto] = producto
        if self._guardar_en_archivo():
            return True, f"Producto '{producto.nombre}' añadido y guardado exitosamente."
        return False, "Producto añadido localmente pero falló el guardado en archivo."

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto not in self.productos:
            return False, "Producto no encontrado."
        
        if cantidad is not None:
            self.productos[id_producto].cantidad = cantidad
        if precio is not None:
            self.productos[id_producto].precio = precio
            
        if self._guardar_en_archivo():
            return True, f"Producto ID {id_producto} actualizado en el archivo."
        return False, "Actualización local exitosa pero falló el guardado en archivo."

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            nombre = self.productos[id_producto].nombre
            del self.productos[id_producto]
            if self._guardar_en_archivo():
                return True, f"Producto '{nombre}' eliminado del inventario y del archivo."
            return False, "Eliminado localmente pero falló la actualización del archivo."
        return False, "Producto no encontrado."

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        return encontrados

    def obtener_todos(self):
        return list(self.productos.values())
