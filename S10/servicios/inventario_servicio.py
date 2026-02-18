from modelos.inventario import Inventario
from modelos.producto import Producto

class InventarioServicio:
    """
    Capa de servicio que actúa como intermediaria entre la UI y el Modelo.
    """
    def __init__(self):
        self.inventario = Inventario()

    def registrar_producto(self, id_p, nombre, cantidad, precio):
        nuevo_producto = Producto(id_p, nombre, cantidad, precio)
        exito, mensaje = self.inventario.agregar_producto(nuevo_producto)
        return exito, mensaje

    def listar_productos(self):
        return self.inventario.obtener_todos()

    def actualizar_stock_o_precio(self, id_p, cantidad=None, precio=None):
        return self.inventario.actualizar_producto(id_p, cantidad, precio)

    def remover_producto(self, id_p):
        return self.inventario.eliminar_producto(id_p)

    def buscar_por_nombre(self, nombre):
        return self.inventario.buscar_producto(nombre)
