# Sistema de Gestión de Inventario



##  Características Principales

El sistema ha sido diseñado para ofrecer una experiencia de usuario eficiente a través de una interfaz de consola intuitiva, integrando las siguientes funcionalidades:

- **Gestión Integral de Productos**: Registro, eliminación y actualización de ítems.
- **Búsqueda Inteligente**: Localización de productos mediante coincidencias de nombre.
- **Persistencia de Datos**: Almacenamiento automático en formato JSON para garantizar que la información no se pierda al cerrar el programa.
- **Validación de Datos**: Control de tipos y unicidad de identificadores para prevenir inconsistencias.

##  Arquitectura del Código

La aplicación se fundamenta en dos pilares principales definidos mediante clases:

### 1. Clase `Producto`
Encapsula la información de cada artículo individual. Utiliza **decoradores de propiedad** (`@property`) para el manejo de atributos, asegurando el principio de encapsulamiento.

| Atributo | Tipo | Descripción |
| :--- | :--- | :--- |
| `ID` | String | Identificador único del producto. |
| `Nombre` | String | Denominación comercial del artículo. |
| `Cantidad` | Integer | Stock disponible en almacén. |
| `Precio` | Float | Valor unitario del producto. |

### 2. Clase `Inventario`
Actúa como el controlador del sistema. Utiliza un **Diccionario** como colección principal para optimizar las búsquedas por ID a una complejidad de tiempo constante $O(1)$.

> "La elección de un diccionario sobre una lista permite que, incluso con miles de productos, la recuperación y actualización de un ítem específico sea instantánea."

##  Almacenamiento y Persistencia

Para el manejo de archivos, se implementó un sistema de **Serialización y Deserialización** utilizando el formato JSON. 

1. **Carga**: Al iniciar, el sistema busca el archivo `inventario.json`. Si existe, reconstruye los objetos `Producto` a partir de los datos almacenados.
2. **Guardado**: Tras cada operación de escritura (añadir, eliminar o actualizar), el sistema sincroniza automáticamente el estado de la colección con el archivo físico.



---
*Desarrollado con un enfoque en la eficiencia de estructuras de datos y principios de ingeniería de software. Y por alguna razon tengo el precentimiento de haber hecho esta actividad en el pasado...*
