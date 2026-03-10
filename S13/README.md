# Sistema Básico de Gestión de Garaje

## 1. Introducción

Este proyecto consiste en el desarrollo de una aplicación de escritorio con interfaz gráfica de usuario (GUI) utilizando la librería `Tkinter` de Python. El objetivo principal es implementar un sistema básico para la gestión de vehículos en un garaje, siguiendo una arquitectura modular basada en los principios de Programación Orientada a Objetos (POO). La aplicación permite registrar vehículos, visualizar la información de los mismos en una tabla y limpiar los campos del formulario de entrada.

## 2. Arquitectura del Proyecto

La aplicación ha sido diseñada siguiendo una arquitectura modular para promover la separación de responsabilidades, la mantenibilidad y la escalabilidad del código. La estructura de directorios y archivos es la siguiente:

```
garaje_app/
│
├── main.py
├── modelos/
│   └── vehiculo.py
├── servicios/
│   └── garaje_servicio.py
└── ui/
    └── app_tkinter.py
```

### 2.1. Módulo `modelos`

Contiene la definición de las clases que representan las entidades de negocio del sistema. En este caso, incluye la clase `Vehiculo`.

*   **`vehiculo.py`**: Define la clase `Vehiculo` con atributos como `placa`, `marca` y `propietario`.

### 2.2. Módulo `servicios`

Encargado de encapsular la lógica de negocio de la aplicación. Interactúa con los modelos para realizar operaciones y gestionar los datos. Aquí se encuentra la clase `GarajeServicio`.

*   **`garaje_servicio.py`**: Implementa métodos para agregar vehículos (`agregar_vehiculo`), obtener la lista de vehículos registrados (`obtener_vehiculos`) y limpiar los registros (`limpiar_registros`). Utiliza una lista en memoria para almacenar los vehículos.

### 2.3. Módulo `ui`

Contiene la implementación de la interfaz gráfica de usuario. Utiliza `Tkinter` para construir la ventana principal, los campos de entrada, botones y la tabla de visualización de vehículos.

*   **`app_tkinter.py`**: Define la clase `AppGaraje`, que hereda de `tk.Tk`. Esta clase se encarga de la creación y disposición de todos los widgets de la interfaz, así como de la gestión de los eventos asociados a los botones.

### 2.4. Archivo `main.py`

Es el punto de entrada de la aplicación. Se encarga de inicializar la interfaz gráfica y de iniciar el bucle principal de eventos de `Tkinter`.

*   **`main.py`**: Importa la clase `AppGaraje` del módulo `ui` y crea una instancia para ejecutar la aplicación.

## 3. Requisitos del Programa

### 3.1. Interfaz Gráfica

La ventana principal de la aplicación incluye los siguientes elementos:

*   **Título de la aplicación**: "Sistema de Gestión de Garaje".
*   **Campos de texto**: Para ingresar la `Placa`, `Marca` y `Propietario` del vehículo.
*   **Botón "Agregar Vehículo"**: Permite registrar un nuevo vehículo en el sistema.
*   **Botón "Limpiar Formulario"**: Borra el contenido de los campos de entrada.
*   **Tabla de Vehículos**: Una `ttk.Treeview` que muestra los vehículos registrados con sus respectivas `Placa`, `Marca` y `Propietario`.

### 3.2. Datos del Vehículo

Cada vehículo se representa con los siguientes atributos:

*   **Placa**: Identificador único del vehículo.
*   **Marca**: Marca del vehículo.
*   **Propietario**: Nombre del propietario del vehículo.

## 4. Requisitos Técnicos

*   **Tkinter**: Utilizado para la construcción de la interfaz gráfica.
*   **Clases y POO**: El diseño del sistema se basa en clases para representar entidades (`Vehiculo`) y encapsular la lógica (`GarajeServicio`, `AppGaraje`).
*   **Eventos de Botones**: Los botones "Agregar Vehículo" y "Limpiar Formulario" están asociados a métodos que manejan sus respectivas acciones.
*   **Organización del Código**: El código está estructurado en los directorios `modelos`, `servicios` y `ui`, y el archivo `main.py` como punto de entrada.

## 5. Cómo Ejecutar la Aplicación

Para ejecutar la aplicación, siga los siguientes pasos:

1.  **Clonar el repositorio** (si aplica) o descargar los archivos del proyecto.
2.  **Navegar al directorio raíz del proyecto** (`garaje_app`).
3.  **Ejecutar el archivo `main.py`** desde la terminal:

    ```bash
    python3 main.py
    ```

    Asegúrese de tener Python 3 instalado en su sistema. La librería `Tkinter` generalmente viene incluida con las instalaciones estándar de Python.

## 6. Criterios de Evaluación (Cumplimiento)

*   **Arquitectura del proyecto**: Se ha utilizado la estructura de carpetas `modelos`, `servicios`, `ui` y `main.py` según lo solicitado.
*   **Funcionamiento del programa**: La aplicación permite agregar vehículos, los muestra en una tabla y los botones funcionan correctamente.
*   **Interfaz gráfica**: Se han utilizado componentes de `Tkinter` para construir una interfaz funcional y clara.
*   **Código**: El código está organizado, es comprensible y sigue los principios de la Programación Orientada a Objetos.

## Autor

**MINAYA GARCIA CRISTOPHER JEFFERSON**
##
POSDATA: LICENCIADO SI ME DICE QUE LE FALTA ALGO DE PLANO DEJO LA PROGRAMACION :'')
