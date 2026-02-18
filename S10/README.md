# Sistema de Gestión de Inventarios Mejorado 

## Introducción

Este proyecto implementa un **Sistema de Gestión de Inventarios** en Python, mejorando una versión anterior con la adición de **persistencia de datos en archivos de texto** y un **manejo robusto de excepciones**. El objetivo es demostrar cómo una aplicación puede almacenar y recuperar su estado de manera fiable, y cómo puede recuperarse elegantemente de errores comunes relacionados con la manipulación de archivos. El sistema sigue los principios de la Programación Orientada a Objetos (POO) y una arquitectura de capas para asegurar la modularidad y mantenibilidad del código.

## Objetivos Cumplidos

*   **Almacenamiento de Inventarios en Archivos**: Todas las modificaciones (añadir, actualizar, eliminar productos) se reflejan automáticamente en el archivo `inventario.txt`.
*   **Recuperación de Inventarios desde Archivos**: Al iniciar, el programa carga automáticamente los productos existentes de `inventario.txt`.
*   **Manejo de Excepciones**: Implementación de bloques `try-except` para gestionar `FileNotFoundError`, `PermissionError` y otros errores inesperados durante las operaciones de archivo.
*   **Creación de Archivo si no Existe**: El sistema crea `inventario.txt` si no lo encuentra al inicio.
*   **Interfaz de Usuario Mejorada**: Notificaciones claras al usuario sobre el éxito o fallo de las operaciones, incluyendo las de archivo.
*   **Organización y Claridad del Código**: Adherencia a la arquitectura de capas (modelos, servicios, main) y uso de comentarios explicativos.

## Arquitectura del Proyecto

El proyecto está estructurado en las siguientes capas, siguiendo las buenas prácticas de diseño de software:

```
sistema_inventario/
├── modelos/
│   ├── producto.py
│   └── inventario.py
├── servicios/
│   └── inventario_servicio.py
└── main.py
```

### 1. Capa de Modelos (`modelos/`)

Contiene las clases que representan las entidades de negocio y la lógica de persistencia de datos.

*   **`producto.py`**: Define la clase `Producto` con atributos como `id_producto`, `nombre`, `cantidad` y `precio`. Incluye métodos `to_line()` y `from_line()` para facilitar la serialización y deserialización de objetos `Producto` a/desde líneas de texto en el archivo.

*   **`inventario.py`**: Define la clase `Inventario`, que gestiona la colección de objetos `Producto`. Es responsable de:
    *   Cargar el inventario desde `inventario.txt` al inicializarse (`_cargar_desde_archivo()`).
    *   Guardar el estado actual del inventario en `inventario.txt` después de cada modificación (`_guardar_en_archivo()`).
    *   Implementar el manejo de excepciones (`FileNotFoundError`, `PermissionError`, `IOError`) para las operaciones de archivo, asegurando que el programa no falle inesperadamente y que el archivo se cree si no existe.
    *   Métodos para agregar, actualizar, eliminar, buscar y listar productos.

### 2. Capa de Servicios (`servicios/`)

Actúa como intermediario entre la interfaz de usuario y los modelos, encapsulando la lógica de negocio y orquestando las operaciones.

*   **`inventario_servicio.py`**: Define la clase `InventarioServicio`. Utiliza una instancia de `Inventario` para realizar las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los productos. Su función principal es abstraer la complejidad de la gestión del inventario de la interfaz de usuario.

### 3. Programa Principal (`main.py`)

Es el punto de entrada de la aplicación. Contiene la interfaz de usuario basada en consola y coordina las interacciones con la capa de servicios.

*   **`main.py`**: Presenta un menú interactivo al usuario. Recoge las entradas del usuario, invoca los métodos apropiados en `InventarioServicio` y muestra los resultados. Implementa manejo de excepciones (`ValueError`) para validar las entradas del usuario (por ejemplo, asegurarse de que la cantidad sea un número entero y el precio un número flotante).

## Manejo de Excepciones Detallado

El sistema incorpora un manejo de excepciones exhaustivo para garantizar su robustez:

*   **En `inventario.py` (`_cargar_desde_archivo` y `_guardar_en_archivo`):**
    *   `FileNotFoundError`: Capturado al intentar leer un archivo que no existe. En este caso, el sistema intenta crear el archivo vacío.
    *   `PermissionError`: Capturado si el programa no tiene los permisos necesarios para leer o escribir en el archivo.
    *   `IOError`: Capturado para errores generales de entrada/salida durante la manipulación del archivo.
    *   `Exception`: Un catch-all para cualquier otro error inesperado durante las operaciones de archivo, proporcionando un mensaje genérico.

*   **En `main.py` (funciones de añadir y actualizar producto):**
    *   `ValueError`: Capturado cuando el usuario introduce datos que no pueden ser convertidos al tipo esperado (por ejemplo, texto en lugar de un número para cantidad o precio).

Cada bloque `try-except` está diseñado para informar al usuario sobre la naturaleza del error, permitiendo una experiencia más amigable y depurable.

## Pruebas Realizadas

Se han realizado pruebas para cubrir los siguientes escenarios:

*   **Inicio con archivo inexistente**: El programa crea `inventario.txt` y funciona correctamente.
*   **Añadir, actualizar y eliminar productos**: Las operaciones se reflejan correctamente en el archivo.
*   **Reinicio del programa**: Los productos previamente guardados se cargan correctamente.
*   **Entrada de datos inválida**: El programa maneja `ValueError` al introducir texto en campos numéricos.
*   **Simulación de `PermissionError`**: (Requiere intervención manual para cambiar permisos del archivo `inventario.txt` a solo lectura) El programa informa sobre la falta de permisos al intentar escribir.

## Conclusión

Este sistema de inventario mejorado demuestra la aplicación práctica de la persistencia de datos y el manejo de excepciones en Python, elementos cruciales para construir aplicaciones robustas y tolerantes a fallos. La arquitectura de capas facilita la comprensión y el mantenimiento, preparando el terreno para futuras expansiones del sistema.
---
---
**POSDATA:** *estoy considerando fuertemente mandarle una gallina criolla para que no mande actividad hasta que termine la Unidad porque de tantas tareas y estres... hasta usted se salva de tener q pasar por eso, asi que que dice, aparte ni se como haya quedado pero capaz que es otro 5 :'v asi que ya ni modo... Diosito en ti confio. Saludos Ing.*
---