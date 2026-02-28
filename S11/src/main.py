from inventario import Inventario
from producto import Producto

def mostrar_menu():
    """Muestra el menú interactivo en la consola."""
    print("\n" + "="*50)
    print("   SISTEMA AVANZADO DE GESTIÓN DE INVENTARIO")
    print("="*50)
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto por Nombre")
    print("5. Mostrar Todo el Inventario")
    print("6. Salir")
    print("="*50)

def ejecutar_sistema():
    """Controlador principal de la interfaz de usuario."""
    # Instancia del controlador de inventario
    inventario = Inventario()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            try:
                id_p = input("ID único: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                
                nuevo_p = Producto(id_p, nombre, cantidad, precio)
                exito, msg = inventario.añadir_producto(nuevo_p)
                print(msg)
            except ValueError as e:
                print(f"Error: Entrada no válida. {e}")

        elif opcion == '2':
            id_p = input("ID del producto a eliminar: ")
            exito, msg = inventario.eliminar_producto(id_p)
            print(msg)

        elif opcion == '3':
            id_p = input("ID del producto a actualizar: ")
            print("Deje en blanco si no desea cambiar el valor.")
            cant_str = input("Nueva cantidad: ")
            prec_str = input("Nuevo precio: ")
            
            try:
                cantidad = int(cant_str) if cant_str else None
                precio = float(prec_str) if prec_str else None
                exito, msg = inventario.actualizar_producto(id_p, cantidad, precio)
                print(msg)
            except ValueError:
                print("Error: La cantidad y el precio deben ser numéricos.")

        elif opcion == '4':
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                print("\nResultados encontrados:")
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            productos = inventario.mostrar_todos()
            if productos:
                print("\nINVENTARIO COMPLETO:")
                print("-" * 50)
                for p in productos:
                    print(p)
                print("-" * 50)
            else:
                print("El inventario está vacío.")

        elif opcion == '6':
            print("Saliendo del sistema... ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    ejecutar_sistema()
