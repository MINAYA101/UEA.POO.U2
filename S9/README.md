# Sistema de Gestión de Inventarios

## 1. Introducción

Este documento detalla el diseño e implementación de un **Sistema de Gestión de Inventarios** simple, desarrollado en Python. El objetivo principal es proporcionar una herramienta básica para que una tienda pueda administrar sus productos, permitiendo operaciones fundamentales como añadir, actualizar, eliminar y buscar artículos. El sistema ha sido concebido siguiendo los principios de la Programación Orientada a Objetos (POO) y una arquitectura modular para facilitar su comprensión y mantenimiento.

## 2. Requisitos del Sistema

El sistema fue diseñado para cumplir con los siguientes requisitos:

*   **Clase `Producto`**: Representa un artículo en el inventario con atributos como ID (único), Nombre, Cantidad y Precio. Incluye un constructor y métodos *getters* y *setters* para cada atributo.
*   **Clase `Inventario`**: Gestiona la colección de productos. Ofrece métodos para añadir nuevos productos (validando la unicidad del ID), eliminar productos por ID, actualizar la cantidad o el precio de un producto por ID, buscar productos por nombre (con coincidencias parciales) y mostrar todos los productos registrados.
*   **Interfaz de Usuario en Consola**: Un menú interactivo que permite al usuario ejecutar todas las operaciones de gestión de inventario de manera sencilla.
*   **Estructura Modular**: El proyecto está organizado en módulos (`modelos/`, `servicios/`, `main.py`) para separar responsabilidades y mejorar la legibilidad del código.

## 3. Arquitectura del Sistema

La arquitectura del proyecto se basa en una estructura modular, dividiendo las responsabilidades en tres componentes principales:

```
sistema_inventario/
├── modelos/
│   ├── __init__.py
│   └── producto.py
├── servicios/
│   ├── __init__.py
│   └── inventario.py
└── main.py
```

*   **`modelos/`**: Contiene las definiciones de las clases que representan las entidades del dominio. En este caso, la clase `Producto`.
*   **`servicios/`**: Aloja la lógica de negocio y las operaciones de gestión del inventario, encapsuladas en la clase `Inventario`.
*   **`main.py`**: Es el punto de entrada de la aplicación. Se encarga de la interacción con el usuario a través de un menú en consola y coordina las llamadas a los servicios del inventario.

Esta separación de preocupaciones facilita la escalabilidad, el mantenimiento y la prueba de cada componente de forma independiente.

## 4. Diseño e Implementación

### 4.1. Clase `Producto`

La clase `Producto` (ubicada en `modelos/producto.py`) es la representación fundamental de un artículo en el inventario. Sus atributos son privados (`__id`, `__nombre`, `__cantidad`, `__precio`) para asegurar el encapsulamiento, y se accede a ellos mediante propiedades (`@property`) para los *getters* y *setters*.

**Atributos:**

*   `__id`: Identificador único del producto. Puede ser `int` o `str`.
*   `__nombre`: Nombre descriptivo del producto.
*   `__cantidad`: Cantidad disponible en stock. Se valida que no sea negativa en el *setter*.
*   `__precio`: Precio unitario del producto. Se valida que no sea negativo en el *setter*.

**Métodos:**

*   `__init__(self, id_producto, nombre, cantidad, precio)`: Constructor que inicializa un nuevo objeto `Producto`.
*   *Getters* (`@property`): `id`, `nombre`, `cantidad`, `precio`.
*   *Setters* (`@id.setter`): `id`, `nombre`, `cantidad`, `precio`. Incluyen validación para `cantidad` y `precio`.
*   `__str__(self)`: Proporciona una representación legible del objeto `Producto` para su impresión.

### 4.2. Clase `Inventario`

La clase `Inventario` (ubicada en `servicios/inventario.py`) es responsable de todas las operaciones de gestión de productos. Mantiene una lista interna de objetos `Producto`.

**Atributos:**

*   `__productos`: Una lista que almacena todas las instancias de `Producto`.

**Métodos:**

*   `__init__(self)`: Inicializa la lista de productos vacía.
*   `añadir_producto(self, producto)`: Añade un `Producto` a la lista. Retorna `(True, mensaje)` si es exitoso o `(False, mensaje)` si el ID ya existe.
*   `eliminar_producto(self, id_producto)`: Busca y elimina un producto por su ID. Retorna `(True, mensaje)` si se elimina o `(False, mensaje)` si no se encuentra.
*   `actualizar_producto(self, id_producto, cantidad=None, precio=None)`: Modifica la cantidad o el precio de un producto. Retorna `(True, mensaje)` si se actualiza o `(False, mensaje)` si no se encuentra.
*   `buscar_por_nombre(self, nombre_parcial)`: Filtra productos cuya nombre coincide parcialmente (ignorando mayúsculas/minúsculas) con el `nombre_parcial` proporcionado. Retorna una lista de `Producto`.
*   `obtener_todos(self)`: Retorna la lista completa de productos en el inventario.

### 4.3. Interfaz de Usuario en Consola (`main.py`)

El archivo `main.py` orquesta la interacción con el usuario. Presenta un menú interactivo y maneja las entradas del usuario para invocar los métodos de la clase `Inventario`.

**Funcionalidades:**

*   **Menú Principal**: Muestra las opciones disponibles (Añadir, Eliminar, Actualizar, Buscar, Listar, Salir).
*   **Manejo de Entradas**: Utiliza funciones auxiliares (`solicitar_entero`, `solicitar_float`) para validar que las entradas numéricas sean correctas.
*   **Limpieza de Pantalla**: Incluye una función (`limpiar_pantalla`) para mantener la consola ordenada.
*   **Flujo de Operaciones**: Cada opción del menú llama a la función correspondiente en la instancia de `Inventario` y muestra mensajes al usuario sobre el resultado de la operación.

## 5. Consideraciones de Desarrollo

Durante el desarrollo, se prestaron especial atención a los siguientes puntos:

*   **Comentarios en el Código**: Se incluyeron comentarios explicativos para describir la lógica de las clases, métodos y funciones, mejorando la legibilidad y comprensión del código.
*   **Validación de Entradas**: Se implementaron validaciones básicas para las entradas del usuario, especialmente para valores numéricos (cantidad y precio), para prevenir errores y mejorar la robustez del sistema.
*   **Organización y Legibilidad**: El código está estructurado de manera clara, con nombres de variables y funciones descriptivos, y siguiendo las convenciones de estilo de Python (PEP 8).
*   **Programación Orientada a Objetos**: Se aplicaron conceptos clave de POO como encapsulamiento (atributos privados y propiedades), abstracción (clases `Producto` e `Inventario`) y modularidad.


## 5. Conclusión

Este Sistema de Gestión de Inventarios cumple con los requisitos establecidos, demostrando la aplicación efectiva de la Programación Orientada a Objetos y una estructura modular. Proporciona una base sólida para futuras expansiones y mejoras, como la persistencia de datos, una interfaz gráfica de usuario o funcionalidades de reporte más avanzadas.

---
***POSDATA:** Diosito en ti confio porque esto minimo merece un 10 y la exoneracion del proximo APE pero como dira que no solo espero que me de puntos extra (tampoco pasara)*