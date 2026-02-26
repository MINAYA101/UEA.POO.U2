import json
import os

class Producto:
    """
    Representa un producto individual en el inventario.
    """
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters y Setters
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
        self._cantidad = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        self._precio = valor

    def to_dict(self):
        """Convierte el objeto a un diccionario para serialización."""
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    @staticmethod
    def from_dict(datos):
        """Crea una instancia de Producto desde un diccionario."""
        return Producto(datos["id"], datos["nombre"], datos["cantidad"], datos["precio"])

    def __str__(self):
        return f"ID: {self._id:5} | Nombre: {self._nombre:20} | Cantidad: {self._cantidad:5} | Precio: ${self._precio:8.2f}"


class Inventario:
    """
    Gestiona la colección de productos y la persistencia de datos.
    """
    def __init__(self, archivo_datos='inventario.json'):
        self.productos = {}  # Diccionario para búsqueda rápida por ID
        self.archivo_datos = archivo_datos
        self.cargar_desde_archivo()

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            return False, f"Error: El ID {producto.id} ya existe."
        self.productos[producto.id] = producto
        self.guardar_en_archivo()
        return True, "Producto añadido exitosamente."

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            return True, "Producto eliminado exitosamente."
        return False, "Error: Producto no encontrado."

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            self.guardar_en_archivo()
            return True, "Producto actualizado exitosamente."
        return False, "Error: Producto no encontrado."

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        return resultados

    def mostrar_todos(self):
        return list(self.productos.values())

    def guardar_en_archivo(self):
        try:
            with open(self.archivo_datos, 'w', encoding='utf-8') as f:
                datos = {id_p: p.to_dict() for id_p, p in self.productos.items()}
                json.dump(datos, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar: {e}")

    def cargar_desde_archivo(self):
        if os.path.exists(self.archivo_datos):
            try:
                with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                    datos = json.load(f)
                    self.productos = {id_p: Producto.from_dict(d) for id_p, d in datos.items()}
            except Exception as e:
                print(f"Error al cargar: {e}")
                self.productos = {}


def mostrar_menu():
    print("\n" + "="*40)
    print("   SISTEMA DE GESTIÓN DE INVENTARIO")
    print("="*40)
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto por Nombre")
    print("5. Mostrar Todo el Inventario")
    print("6. Salir")
    print("="*40)

def ejecutar_sistema():
    inventario = Inventario()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                id_p = input("ID único: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                nuevo_p = Producto(id_p, nombre, cantidad, precio)
                exito, msg = inventario.añadir_producto(nuevo_p)
                print(msg)
            except ValueError:
                print("Error: Cantidad debe ser entero y precio debe ser numérico.")

        elif opcion == '2':
            id_p = input("ID del producto a eliminar: ")
            exito, msg = inventario.eliminar_producto(id_p)
            print(msg)

        elif opcion == '3':
            id_p = input("ID del producto a actualizar: ")
            print("Deje en blanco si no desea cambiar el valor.")
            cant_str = input("Nueva cantidad: ")
            prec_str = input("Nuevo precio: ")
            
            cantidad = int(cant_str) if cant_str else None
            precio = float(prec_str) if prec_str else None
            
            exito, msg = inventario.actualizar_producto(id_p, cantidad, precio)
            print(msg)

        elif opcion == '4':
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                print("\nResultados encontrados:")
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos.")

        elif opcion == '5':
            productos = inventario.mostrar_todos()
            if productos:
                print("\nINVENTARIO COMPLETO:")
                for p in productos:
                    print(p)
            else:
                print("El inventario está vacío.")

        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    ejecutar_sistema()
