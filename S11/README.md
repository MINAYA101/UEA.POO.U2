# Sistema Avanzado de Gestión de Inventario 

Este aplicativo representa una solución de ingeniería de software para la administración de existencias, diseñada bajo un enfoque **Modular y Orientado a Objetos (POO)** en Python. La arquitectura separa claramente la lógica de datos, la gestión de negocio y la interfaz de usuario.

## Arquitectura Modular del Proyecto

El sistema se divide en tres módulos principales para garantizar la escalabilidad y el mantenimiento:

| Módulo | Archivo | Responsabilidad |
| :--- | :--- | :--- |
| **Entidad** | `producto.py` | Define la clase `Producto`, sus atributos, validaciones y métodos de serialización. |
| **Controlador** | `inventario.py` | Gestiona la colección de productos (Diccionario), la lógica de negocio y la persistencia en archivos JSON. |
| **Interfaz** | `main.py` | Implementa el menú interactivo y la comunicación con el usuario final. |

## Características Técnicas

### 1. Programación Orientada a Objetos (POO)
Se aplican principios fundamentales de POO:
- **Encapsulamiento**: Uso de atributos protegidos (`_id`, `_nombre`, etc.) y decoradores `@property` para controlar el acceso y validación de datos.
- **Abstracción**: Separación de la representación del producto de su gestión en el inventario.

### 2. Gestión Eficiente con Colecciones
El sistema utiliza un **Diccionario** (`dict`) como estructura de datos central. Esta elección técnica permite:
- **Búsqueda por ID**: Complejidad de tiempo $O(1)$, garantizando un rendimiento óptimo sin importar el tamaño del inventario.
- **Búsqueda por Nombre**: Implementada mediante *List Comprehensions* para un filtrado rápido y legible.

### 3. Persistencia de Datos
La información se almacena en un archivo `inventario.json`. El proceso incluye:
- **Serialización**: Conversión de objetos `Producto` a diccionarios compatibles con JSON.
- **Deserialización**: Reconstrucción automática de los objetos al iniciar la aplicación.



---
*Desarrollado con un enfoque en la modularidad, eficiencia de estructuras de datos y principios de ingeniería de software... para nada tube que actualizar el codigo porque quice hacerlo en un solo archivo...*
