class Producto:
    """
    Representa un producto individual en el inventario.
    """
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

    def to_line(self):
        """Convierte el objeto a una línea de texto para el archivo."""
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}\n"

    @staticmethod
    def from_line(line):
        """Crea un objeto Producto a partir de una línea de texto del archivo."""
        partes = line.strip().split(',')
        if len(partes) == 4:
            return Producto(partes[0], partes[1], int(partes[2]), float(partes[3]))
        return None
