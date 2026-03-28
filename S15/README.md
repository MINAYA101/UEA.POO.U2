# Informe Técnico: Aplicación de Gestión de Tareas (To-Do List)

## 1. Introducción
El presente documento detalla el diseño y la implementación de una aplicación de escritorio para la gestión de tareas diarias, desarrollada bajo el lenguaje de programación **Python** y la biblioteca de interfaz gráfica **Tkinter**. El objetivo principal del proyecto es demostrar la aplicación de una arquitectura modular por capas, el manejo avanzado de eventos de usuario y la separación de responsabilidades en el desarrollo de software.

## 2. Arquitectura del Sistema
La aplicación se ha estructurado siguiendo un patrón de diseño modular que garantiza la escalabilidad y el mantenimiento del código. Se han definido tres capas principales, cada una con una responsabilidad única y bien definida:

| Capa | Archivo | Responsabilidad |
| :--- | :--- | :--- |
| **Modelo** | `modelos/tarea.py` | Define la entidad `Tarea` y sus atributos fundamentales (ID, descripción, estado). |
| **Servicio** | `servicios/tarea_servicio.py` | Implementa la lógica de negocio, gestionando la persistencia en memoria y las operaciones CRUD. |
| **Interfaz (UI)** | `ui/app_tkinter.py` | Gestiona la presentación visual, la captura de eventos y la interacción directa con el usuario. |
| **Orquestador** | `main.py` | Punto de entrada del sistema que inicializa las dependencias y arranca el bucle principal de la aplicación. |

## 3. Implementación Técnica

### 3.1. Capa de Modelo
La clase `Tarea` actúa como un contenedor de datos. Se ha implementado un constructor que permite inicializar cada tarea con un identificador único y un estado de completado por defecto en falso.

> "La separación del modelo asegura que la estructura de los datos sea independiente de cómo se muestran o se procesan."

### 3.2. Capa de Servicio
La clase `TareaServicio` centraliza la lógica de manipulación de datos. Utiliza una lista interna para almacenar los objetos `Tarea` y métodos específicos para:
*   **Agregar**: Instancia nuevas tareas asignando IDs incrementales.
*   **Completar**: Localiza una tarea por su ID y actualiza su estado booleano.
*   **Eliminar**: Filtra la lista para remover la tarea especificada.
*   **Listar**: Retorna la colección actual de tareas para su visualización.

### 3.3. Capa de Interfaz de Usuario (GUI)
La interfaz se ha construido utilizando componentes avanzados de `tkinter.ttk` para un acabado profesional. Se destacan las siguientes funcionalidades técnicas:

*   **Manejo de Eventos**:
    >   **Teclado**: Se ha vinculado la tecla `<Return>` (Enter) al campo de entrada para permitir la adición rápida de tareas sin necesidad de usar el ratón.
    >   **Ratón**: Se implementó el evento `<Double-1>` (doble clic) sobre los elementos de la lista (`Treeview`) para marcar tareas como completadas de forma intuitiva.
*   **Feedback Visual**: Mediante el uso de *tags* en el componente `Treeview`, las tareas completadas cambian dinámicamente su apariencia (color gris y fuente tachada), proporcionando una confirmación visual inmediata al usuario.

## 4. Conclusión
La implementación exitosa de este proyecto demuestra que el uso de una arquitectura por capas no solo organiza el código, sino que facilita la depuración y futuras extensiones del sistema. La integración de manejadores de eventos avanzados mejora significativamente la experiencia del usuario, cumpliendo con los estándares modernos de aplicaciones de escritorio.
Posdata: Ing. y si la proxima semana no manda tarea? y decimos que hubo un fallo en la matrix y los servidores y por eso no se refleja en el moddle :'D ??

---
