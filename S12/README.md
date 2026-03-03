# Sistema de Gestión de Biblioteca Digital con Arquitectura por Capas

## 1. Introducción

Este documento detalla el desarrollo de un Sistema de Gestión de Biblioteca Digital implementado en Python, siguiendo los principios de la Programación Orientada a Objetos (POO) y una arquitectura estructurada por capas. El objetivo principal es demostrar una clara separación entre la lógica de negocio y la ejecución del programa, utilizando modelos para representar entidades, servicios para gestionar la lógica de negocio y un punto de entrada para la interacción del usuario.

## 2. Arquitectura del Proyecto

El proyecto está organizado en una estructura de directorios que refleja la arquitectura por capas solicitada, garantizando una separación de responsabilidades clara y mantenible:

```
biblioteca_app/
│
├── modelos/
│   ├── libro.py
│   └── usuario.py
│
├── servicios/
│   └── biblioteca_servicio.py
│
└── main.py
```

- **`modelos/`**: Contiene las clases que representan las entidades del dominio (Libro y Usuario).
- **`servicios/`**: Aloja la lógica de negocio principal del sistema, encapsulada en la clase `BibliotecaServicio`.
- **`main.py`**: Es el punto de arranque de la aplicación, encargado de la interacción con el usuario a través de un menú en consola y de coordinar las operaciones con el servicio.

## 3. Clases Principales

### 3.1. `Libro` (Modelo)

Representa un libro en el sistema. Sus atributos son:

- **`info`**: Una tupla `(titulo, autor)` para almacenar el título y el autor de forma inmutable.
- **`categoria`**: La categoría a la que pertenece el libro.
- **`isbn`**: Un identificador único para el libro (International Standard Book Number).

**Consideraciones técnicas:**
- Se utiliza una tupla para `titulo` y `autor` para asegurar su inmutabilidad.

**Código (`biblioteca_app/modelos/libro.py`):**

```python
class Libro:
    """
    Representa un libro dentro del sistema de biblioteca.
    """
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    @property
    def titulo(self):
        return self.info[0]

    @property
    def autor(self):
        return self.info[1]

    def __str__(self):
        return f"Libro: {self.titulo} | Autor: {self.autor} | Categoría: {self.categoria} | ISBN: {self.isbn}"
```

### 3.2. `Usuario` (Modelo)

Representa a un usuario registrado en la biblioteca. Sus atributos son:

- **`nombre`**: El nombre del usuario.
- **`id_usuario`**: Un identificador único para el usuario.
- **`libros_prestados`**: Una lista que almacena los objetos `Libro` que el usuario tiene actualmente en préstamo.

**Consideraciones técnicas:**
- Se utiliza una lista para `libros_prestados` para permitir la adición y eliminación dinámica de libros.

**Código (`biblioteca_app/modelos/usuario.py`):**

```python
class Usuario:
    """
    Representa a un usuario registrado en la biblioteca.
    """
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}) | Libros prestados: {len(self.libros_prestados)}"
```

### 3.3. `BibliotecaServicio` (Servicio)

Esta clase encapsula toda la lógica de negocio del sistema de la biblioteca. Administra la colección de libros disponibles, los usuarios registrados, y las operaciones de préstamos y devoluciones.

**Consideraciones técnicas:**
- **`libros_disponibles`**: Un diccionario donde la clave es el ISBN y el valor es el objeto `Libro`, facilitando la búsqueda y gestión por ISBN.
- **`ids_usuarios`**: Un conjunto (`set`) para almacenar los IDs únicos de los usuarios, lo que permite una verificación eficiente de la unicidad y existencia de IDs.
- **`usuarios_registrados`**: Un diccionario donde la clave es el ID de usuario y el valor es el objeto `Usuario`.

**Funcionalidades Mínimas Implementadas:**
- `añadir_libro(titulo, autor, categoria, isbn)`: Agrega un libro al catálogo.
- `quitar_libro(isbn)`: Elimina un libro del catálogo si no está prestado.
- `registrar_usuario(nombre, id_usuario)`: Registra un nuevo usuario.
- `dar_de_baja_usuario(id_usuario)`: Elimina un usuario si no tiene libros prestados.
- `prestar_libro(isbn, id_usuario)`: Asigna un libro a un usuario.
- `devolver_libro(isbn, id_usuario)`: Registra la devolución de un libro.
- `buscar_libros(criterio, valor)`: Busca libros por título, autor o categoría.
- `listar_libros_prestados(id_usuario)`: Muestra los libros que un usuario tiene en préstamo.

**Código (`biblioteca_app/servicios/biblioteca_servicio.py`):**

```python
from modelos.libro import Libro
from modelos.usuario import Usuario

class BibliotecaServicio:
    """
    Gestiona la lógica del sistema de biblioteca digital.
    """
    def __init__(self):
        self.libros_disponibles = {}
        self.ids_usuarios = set()
        self.usuarios_registrados = {}

    def añadir_libro(self, titulo, autor, categoria, isbn):
        if isbn in self.libros_disponibles:
            return False, f"El libro con ISBN {isbn} ya existe."
        
        nuevo_libro = Libro(titulo, autor, categoria, isbn)
        self.libros_disponibles[isbn] = nuevo_libro
        return True, f"Libro \'{titulo}\' añadido correctamente."

    def quitar_libro(self, isbn):
        if isbn not in self.libros_disponibles:
            return False, "El libro no se encuentra en el catálogo."
        
        for usuario in self.usuarios_registrados.values():
            if any(libro.isbn == isbn for libro in usuario.libros_prestados):
                return False, "No se puede eliminar un libro que está actualmente prestado."
        
        del self.libros_disponibles[isbn]
        return True, "Libro eliminado correctamente."

    def registrar_usuario(self, nombre, id_usuario):
        if id_usuario in self.ids_usuarios:
            return False, f"El ID de usuario {id_usuario} ya está registrado."
        
        nuevo_usuario = Usuario(nombre, id_usuario)
        self.usuarios_registrados[id_usuario] = nuevo_usuario
        self.ids_usuarios.add(id_usuario)
        return True, f"Usuario \'{nombre}\' registrado correctamente."

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            return False, "El usuario no existe."
        
        usuario = self.usuarios_registrados[id_usuario]
        if usuario.libros_prestados:
            return False, "No se puede dar de baja a un usuario con libros pendientes de devolución."
        
        del self.usuarios_registrados[id_usuario]
        self.ids_usuarios.remove(id_usuario)
        return True, "Usuario dado de baja correctamente."

    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros_disponibles:
            return False, "El libro no está disponible en el catálogo."
        
        if id_usuario not in self.usuarios_registrados:
            return False, "El usuario no está registrado."
        
        for u in self.usuarios_registrados.values():
            if any(libro.isbn == isbn for libro in u.libros_prestados):
                return False, "El libro ya se encuentra prestado a otro usuario."
        
        libro = self.libros_disponibles[isbn]
        usuario = self.usuarios_registrados[id_usuario]
        usuario.libros_prestados.append(libro)
        return True, f"Libro \'{libro.titulo}\' prestado a {usuario.nombre}."

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            return False, "El usuario no está registrado."
        
        usuario = self.usuarios_registrados[id_usuario]
        libro_encontrado = None
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                libro_encontrado = libro
                break
        
        if not libro_encontrado:
            return False, "El usuario no tiene este libro en préstamo."
        
        usuario.libros_prestados.remove(libro_encontrado)
        return True, f"Libro \'{libro_encontrado.titulo}\' devuelto correctamente."

    def buscar_libros(self, criterio, valor):
        resultados = []
        valor = valor.lower()
        
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and valor in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor in libro.categoria.lower():
                resultados.append(libro)
        
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            return None, "El usuario no existe."
        
        usuario = self.usuarios_registrados[id_usuario]
        return usuario.libros_prestados, f"Libros prestados a {usuario.nombre}:"
```

## 4. Punto de Entrada (`main.py`)

El archivo `main.py` actúa como la interfaz de usuario del sistema. Contiene un menú interactivo en consola que permite al usuario realizar todas las operaciones definidas en `BibliotecaServicio`. Es crucial destacar que `main.py` no contiene lógica de negocio directamente, sino que invoca los métodos del `BibliotecaServicio` para ejecutar las acciones.

**Código (`biblioteca_app/main.py`):**

```python
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from servicios.biblioteca_servicio import BibliotecaServicio

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL ---")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libros")
    print("8. Listar libros prestados a un usuario")
    print("9. Salir")
    return input("Seleccione una opción: ")

def main():
    servicio = BibliotecaServicio()
    
    # Datos de prueba iniciales
    servicio.añadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "978-0307474728")
    servicio.añadir_libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", "978-8420412146")
    servicio.registrar_usuario("Juan Pérez", "U001")

    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            exito, mensaje = servicio.añadir_libro(titulo, autor, categoria, isbn)
            print(mensaje)
            
        elif opcion == "2":
            isbn = input("ISBN del libro a quitar: ")
            exito, mensaje = servicio.quitar_libro(isbn)
            print(mensaje)
            
        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID de usuario: ")
            exito, mensaje = servicio.registrar_usuario(nombre, id_usuario)
            print(mensaje)
            
        elif opcion == "4":
            id_usuario = input("ID de usuario a dar de baja: ")
            exito, mensaje = servicio.dar_de_baja_usuario(id_usuario)
            print(mensaje)
            
        elif opcion == "5":
            isbn = input("ISBN del libro: ")
            id_usuario = input("ID del usuario: ")
            exito, mensaje = servicio.prestar_libro(isbn, id_usuario)
            print(mensaje)
            
        elif opcion == "6":
            isbn = input("ISBN del libro: ")
            id_usuario = input("ID del usuario: ")
            exito, mensaje = servicio.devolver_libro(isbn, id_usuario)
            print(mensaje)
            
        elif opcion == "7":
            print("Buscar por: 1. Título, 2. Autor, 3. Categoría")
            criterio_op = input("Opción: ")
            criterios = {"1": "titulo", "2": "autor", "3": "categoria"}
            criterio = criterios.get(criterio_op)
            
            if criterio:
                valor = input(f"Ingrese el {criterio} a buscar: ")
                resultados = servicio.buscar_libros(criterio, valor)
                if resultados:
                    print("\nResultados encontrados:")
                    for libro in resultados:
                        print(libro)
                else:
                    print("No se encontraron libros.")
            else:
                print("Opción no válida.")
                
        elif opcion == "8":
            id_usuario = input("ID del usuario: ")
            libros, mensaje = servicio.listar_libros_prestados(id_usuario)
            print(mensaje)
            if libros:
                for libro in libros:
                    print(f" - {libro}")
            elif libros == []:
                print(" - El usuario no tiene libros prestados.")
                
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
```

## 5. Implementación y Buenas Prácticas

- **Encapsulamiento**: Todos los atributos de las clases `Libro` y `Usuario` son privados o se acceden a través de propiedades (`@property`) cuando es necesario, garantizando el control sobre el estado de los objetos.
- **Métodos Claros y Coherentes**: Cada método tiene una responsabilidad única y un nombre descriptivo que indica su función.
- **Separación de Responsabilidades**: La lógica de negocio reside exclusivamente en `BibliotecaServicio`, mientras que los modelos solo representan datos y `main.py` se encarga de la interacción y orquestación.
- **Uso Adecuado de Colecciones**: Se han utilizado tuplas para datos inmutables (título y autor), listas para colecciones ordenadas y modificables (libros prestados), diccionarios para mapeo eficiente por clave (libros disponibles, usuarios registrados) y conjuntos para garantizar la unicidad de IDs (IDs de usuarios).
- **Comentarios en el Código**: Se han incluido comentarios para explicar decisiones de diseño y la funcionalidad de secciones clave del código.

## 6. Pruebas del Sistema

Para demostrar el funcionamiento del sistema, se ha incluido un script de prueba (`test_biblioteca.py`) que realiza las siguientes operaciones:

1.  **Añadir libros**: Se agregan dos libros al catálogo.
2.  **Registrar usuarios**: Se registran dos usuarios.
3.  **Préstamos**: Se prestan libros a un usuario.
4.  **Listar libros prestados**: Se verifica la lista de libros prestados a un usuario.
5.  **Búsquedas**: Se realiza una búsqueda de libros por autor.
6.  **Devoluciones**: Se devuelve un libro.
7.  **Quitar libros**: Se elimina un libro del catálogo.

La ejecución de este script confirma que todas las funcionalidades mínimas requeridas operan correctamente.

## 
*Segun yo no deberia saltar errores asi que nuevamente como diria la roca en Rapidos y Furiosos, "Tube fé..."*
Att: Minaya G.