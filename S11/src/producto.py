class Producto:
    """
    Clase que representa un producto individual en el inventario.
    Aplica el principio de encapsulamiento mediante el uso de propiedades.
    """
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters y Setters con decoradores @property
    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if valor < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self._cantidad = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = valor

    def to_dict(self):
        """Convierte el objeto a un diccionario para facilitar la serialización JSON."""
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    @staticmethod
    def from_dict(datos):
        """Crea una instancia de Producto a partir de un diccionario de datos."""
        return Producto(
            datos["id"], 
            datos["nombre"], 
            datos["cantidad"], 
            datos["precio"]
        )

    def __str__(self):
        """Representación formal del producto para visualización en consola."""
        return f"ID: {self._id:5} | Nombre: {self._nombre:20} | Stock: {self._cantidad:5} | Precio: ${self._precio:8.2f}"
