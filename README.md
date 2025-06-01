# Calculadora CPM - Método de la Ruta Crítica

Este proyecto es una sencilla aplicación web construida con **Flask** que permite a los usuarios calcular el **Método de la Ruta Crítica (CPM)** para las actividades de un proyecto. Ayuda a identificar la secuencia más larga de actividades que deben completarse a tiempo para que todo el proyecto finalice según lo programado.

## Características

* **Entrada de Actividades:** Añade fácilmente las actividades del proyecto con sus nombres, duraciones y predecesoras.
* **Cálculo CPM:** Calcula el **Tiempo de Inicio Más Temprano (TIP)**, el **Tiempo de Terminación Más Tardío (TTT)** y la **Holgura** para cada actividad.
* **Identificación de la Ruta Crítica:** Resalta la ruta crítica, que se compone de actividades con holgura cero.
* **Adición Dinámica de Filas:** Añade más filas de entrada de actividades según sea necesario con un solo clic.
* **Interfaz de Usuario Amigable:** Una interfaz web limpia e intuitiva para la entrada de datos y la visualización de resultados.

---

## Tecnologías Utilizadas

* **Flask:** Un marco web ligero de Python.
* **HTML/CSS:** Para estructurar y dar estilo a la interfaz web.
* **JavaScript:** Para la funcionalidad dinámica del lado del cliente (por ejemplo, añadir filas).
* **Pandas (opcional):** Aunque está en los `requirements`, no se usa directamente en la lógica CPM actual, pero es una librería útil para manejo de datos en Python.

---

## Configuración e Instalación

Para ejecutar este proyecto localmente, sigue estos pasos:

1.  **Clona el repositorio** (o descarga los archivos `app.py` y la carpeta `templates`):

    ```bash
    git clone <url_del_repositorio> # Si tienes un repositorio Git
    cd <nombre_de_tu_carpeta_proyecto>
    ```

2.  **Crea un entorno virtual (opcional):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # En sistemas Unix/macOS
    .\venv\Scripts\activate   # En Windows (CMD)
    ```

3.  **Instala las dependencias necesarias:**

    ```bash
    pip install Flask pandas
    ```

4.  **Ejecuta la aplicación Flask:**

    ```bash
    python app.py
    ```

    La aplicación se iniciará y estará disponible en `http://127.0.0.1:5055/`. Abre esta URL en tu navegador web.

---

## Uso

1.  **Ingresa las Actividades:** En la tabla, rellena el "Actividad" (Nombre de la Actividad), "Precedentes" (Actividades predecesoras, separadas por comas si hay varias, ej: `A, B`) y "Duración" (Duración de la actividad en unidades de tiempo).
2.  **Añade Filas:** Si necesitas más filas para ingresar actividades, haz clic en el botón "Agregar fila".
3.  **Calcula el CPM:** Haz clic en el botón "Calcular CPM" para procesar los datos y ver los resultados.
4.  **Visualiza los Resultados:** La sección de resultados mostrará una tabla con el Tiempo de Inicio Más Temprano (TIP), el Tiempo de Terminación Más Tardío (TTT) y la Holgura para cada actividad, junto con la **Ruta Crítica** identificada.

---

## Estructura del Proyecto

* `app.py`: Contiene la lógica principal de la aplicación Flask, la clase `Activity` y las funciones para el cálculo del CPM.
* `templates/`: Carpeta que almacena las plantillas HTML.
    * `index.html`: La interfaz de usuario principal de la aplicación.

---

## Créditos

**Desarrollado por:**

* **Luis Martines**
* **Edgar Montes**

**Corporación Universitaria del Caribe - CECAR**
© 2025

---