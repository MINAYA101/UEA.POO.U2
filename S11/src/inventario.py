import json
import os
from producto import Producto

class Inventario:
    """
    Clase controladora que gestiona la colección de productos y la persistencia en archivos.
    Utiliza un diccionario para optimizar las búsquedas por ID (O(1)).
    """
    def __init__(self, archivo_datos='inventario.json'):
        self._productos = {}  # Colección principal: Diccionario {ID: Objeto Producto}
        self._archivo_datos = archivo_datos
        self.cargar_desde_archivo()

    def añadir_producto(self, producto):
        """Añade un nuevo producto al inventario si el ID no existe."""
        if producto.id in self._productos:
            return False, f"Error: El ID {producto.id} ya está registrado."
        self._productos[producto.id] = producto
        self.guardar_en_archivo()
        return True, "Producto añadido exitosamente."

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        if id_producto in self._productos:
            del self._productos[id_producto]
            self.guardar_en_archivo()
            return True, "Producto eliminado exitosamente."
        return False, "Error: Producto no encontrado."

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza los atributos de un producto existente."""
        if id_producto in self._productos:
            try:
                if cantidad is not None:
                    self._productos[id_producto].cantidad = cantidad
                if precio is not None:
                    self._productos[id_producto].precio = precio
                self.guardar_en_archivo()
                return True, "Producto actualizado exitosamente."
            except ValueError as e:
                return False, f"Error de validación: {e}"
        return False, "Error: Producto no encontrado."

    def buscar_por_nombre(self, nombre):
        """Busca productos cuyo nombre contenga la cadena especificada."""
        # Uso de list comprehension para búsqueda eficiente en la colección
        resultados = [p for p in self._productos.values() if nombre.lower() in p.nombre.lower()]
        return resultados

    def mostrar_todos(self):
        """Retorna una lista con todos los productos del inventario."""
        return list(self._productos.values())

    def guardar_en_archivo(self):
        """Serializa la colección de productos a un archivo JSON."""
        try:
            with open(self._archivo_datos, 'w', encoding='utf-8') as f:
                # Serialización de cada objeto Producto a diccionario
                datos = {id_p: p.to_dict() for id_p, p in self._productos.items()}
                json.dump(datos, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error crítico al guardar datos: {e}")

    def cargar_desde_archivo(self):
        """Deserializa los datos del archivo JSON y reconstruye los objetos Producto."""
        if os.path.exists(self._archivo_datos):
            try:
                with open(self._archivo_datos, 'r', encoding='utf-8') as f:
                    datos = json.load(f)
                    # Reconstrucción de objetos Producto desde diccionarios
                    self._productos = {id_p: Producto.from_dict(d) for id_p, d in datos.items()}
            except Exception as e:
                print(f"Error al cargar el archivo de datos: {e}")
                self._productos = {}
