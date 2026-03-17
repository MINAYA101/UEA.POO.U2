# Sistema de Registro de Visitantes 

## 1. Introducción

Como en la actividad anterior, este proyecto implementa una aplicación de escritorio con interfaz gráfica de usuario (GUI) utilizando `Tkinter` en Python. El objetivo es gestionar el registro de visitantes a una oficina, aplicando una arquitectura modular por capas (Modelos, Servicios, UI y Main) para separar claramente las responsabilidades y facilitar la mantenibilidad del código. La aplicación permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) básicas sobre los registros de visitantes, que se almacenan en memoria.

## 2. Arquitectura del Proyecto

La aplicación sigue una arquitectura modular estricta, dividida en las siguientes capas:

```
visitas_app/
│
├── main.py                # Punto de entrada de la aplicación
├── modelos/
│   └── visitante.py       # Define la clase Visitante (Capa de Datos)
├── servicios/
│   └── visita_servicio.py # Contiene la lógica de negocio (Capa de Lógica)
└── ui/
    └── app_tkinter.py     # Implementa la interfaz gráfica (Capa de Presentación)
```

### 2.1. Módulo `modelos`

Contiene la definición de la clase `Visitante`, que representa la entidad de datos principal del sistema.

*   **`visitante.py`**: Define la clase `Visitante` con los atributos `cedula` (identificador único), `nombre` completo y `motivo` de la visita.

### 2.2. Módulo `servicios`

Esta capa encapsula la lógica de negocio y las operaciones CRUD. Gestiona una lista interna de objetos `Visitante`.

*   **`visita_servicio.py`**: Implementa la clase `VisitaServicio` con métodos para:
    *   `registrar_visitante(cedula, nombre, motivo)`: Agrega un nuevo visitante, incluyendo validaciones para campos vacíos y cédulas duplicadas.
    *   `obtener_visitantes()`: Retorna la lista actual de visitantes registrados.
    *   `eliminar_visitante(cedula)`: Elimina un visitante de la lista basándose en su cédula.

### 2.3. Módulo `ui`

Contiene la implementación de la interfaz gráfica de usuario utilizando `Tkinter`.

*   **`app_tkinter.py`**: Define la clase `AppVisitas`, que hereda de `tk.Tk`. Esta clase es responsable de:
    *   Crear y organizar todos los widgets de la interfaz (campos de entrada, botones, tabla `ttk.Treeview`).
    *   Manejar los eventos de los botones (`Registrar`, `Eliminar`, `Limpiar`).
    *   Utilizar `messagebox` para mostrar mensajes al usuario (éxito, advertencias, errores).
    *   Implementa **Inyección de Dependencias** al recibir una instancia de `VisitaServicio` en su constructor, lo que desacopla la UI de la lógica de negocio.

### 2.4. Archivo `main.py`

Es el punto de entrada principal de la aplicación. Se encarga de orquestar la inicialización de las capas de servicio y UI.

*   **`main.py`**: Crea una instancia de `VisitaServicio` y luego la inyecta en el constructor de `AppVisitas`, para finalmente iniciar el bucle principal de `Tkinter`.

## 3. Requisitos del Programa (Cumplimiento)

### 3.1. Interfaz Gráfica (Capa UI)

*   **Formulario de Entrada**: Campos de texto para Cédula, Nombre completo y Motivo de la visita.
*   **Panel de Acciones**: Botones "Registrar Visitante", "Eliminar Seleccionado" y "Limpiar Campos".
*   **Visualización de Datos**: Una tabla `ttk.Treeview` que muestra los visitantes registrados con sus atributos.
*   **Validaciones Visuales**: Uso de `messagebox.showinfo`, `messagebox.showwarning` y `messagebox.showerror` para feedback al usuario.
*   **Marca de Agua**: Un texto en la parte inferior de la ventana indicando la autoría y versión de la aplicación.

### 3.2. Atributos del Visitante (Capa Modelo)

Cada `Visitante` tiene los atributos:

*   `cedula` (string, identificador único)
*   `nombre` (string)
*   `motivo` (string)

### 3.3. Arquitectura del Proyecto

Se ha respetado estrictamente la jerarquía de archivos y la separación de capas solicitada.

## 4. Requisitos Técnicos (Cumplimiento)

*   **Programación Orientada a Objetos (POO)**: Uso extensivo de clases, constructores (`__init__`) y métodos en todas las capas.
*   **Inyección de Dependencias**: La clase `AppVisitas` (UI) recibe la instancia de `VisitaServicio` en su constructor, demostrando un acoplamiento bajo.
*   **Encapsulamiento**: La lista de visitantes (`__visitantes`) en `VisitaServicio` es privada, gestionada internamente por los métodos del servicio.
*   **Sin librerías externas**: Solo se utilizan `tkinter` y `ttk` (parte de `tkinter`), que son librerías estándar de Python.

## Autor

**MINAYA GARCIA CRISTOPHER JEFFERSON**
