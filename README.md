# Rick and Morty Character Explorer

[Español abajo](#explorador-de-personajes-de-rick-y-morty)

## Project Overview
This is a lightweight web application that allows users to interact with the [Rick and Morty API](https://rickandmortyapi.com/). It provides an interface to browse characters, search for them by name, and permanently save favorite characters into a local database.

## Features
- **Browse:** Navigate through paginated lists of characters fetched directly from the external API.
- **Search:** Find specific characters instantly via their name.
- **Favorites Management:** 
  - Save any character to your personal "Favorites" list in a local SQLite database. Ensure duplicated characters are not added.
  - Delete characters from the favorites list.

## Technologies Used
- **Backend:** Python 3, Flask, Flask-SQLAlchemy (for ORM interactions)
- **Frontend:** HTML5, Jinja2 Templates (Server-Side Rendering)
- **Database:** SQLite (local instance database)
- **External Dependencies:** `requests` module to query public APIs

## Architecture
- `app.py`: Acts as the main controller. It handles all routing, HTTP request interpretation (GET parameters for search/pagination and POST parameters for database actions), API fetching logic, and bridging variables over to Jinja templates.
- `models.py`: Defines the database schema representing the `Favorite` entity mapping characters' data traits (ID, API ID, Name, Photo) to table columns using SQLAlchemy.
- `templates/`: Contains the visual structures rendered to clients (`index.html` for main explorative views, and `favorites.html` to manage saved entries). 

## Setup Instructions
1. Clone the repository to your local machine.
2. (Optional but recommended) Create and activate a Virtual Environment.
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application bundle. SQLAlchemy will automatically create the database `.db` file in an `instance` folder upon first initialization.
   ```bash
   python app.py
   ```
5. Open your browser and navigate to `http://127.0.0.1:5000/`.

---

# Explorador de Personajes de Rick y Morty

[English above](#rick-and-morty-character-explorer)

## Resumen del Proyecto
Esta es una aplicación web ágil que permite a los usuarios interactuar con la la [API de Rick and Morty](https://rickandmortyapi.com/). Ofrece una interfaz gráfica lista para navegar entre el listado de personajes, realizar búsquedas mediante el nombre y almacenar personajes en una base de datos local para conservarlos como favoritos.

## Características Principales
- **Exploración:** Navega de forma natural dentro de las páginas de listados proveídas directamente desde la API externa.
- **Búsqueda Avanzada:** Encuentra personajes específicos de manera instantánea utilizando parámetros de nombre.
- **Administración de Favoritos:** 
  - Guarda cualquier personaje dentro de una lista personal de "Favoritos" que residen en una base de datos de tipo SQLite. Evita duplicaciones para la misma selección.
  - Elimina personajes permanentemente de esta lista cuando ya no se deseen allí.

## Tecnologías Implementadas
- **Backend:** Python 3, Flask, Flask-SQLAlchemy (utilizado para interacciones con el modelo de base de datos tipo ORM).
- **Frontend:** HTML5, Plantillas Jinja2 (Renderizado desde el lado del servidor / Server-Side Rendering).
- **Relacional de Datos:** Motor SQLite (implementado sobre instancia local en archivo).
- **Dependencias Externas:** El módulo `requests` para obtener información desde APIs web públicas.

## Arquitectura Funcional
- `app.py`: Actúa como controlador principal. Maneja las rutas (routing), la interpretación de peticiones HTTP (parámetros GET para búsquedas/paginación y peticiones POST para acciones frente a la base de datos), establece la lógica para consultas a la API e inyecta las variables sobre las diferentes plantillas.
- `models.py`: Define el esquema físico de la base de datos, puntualmente representando a la entidad `Favorite` el cual mapea la abstracción de rasgos de los personajes (ID, identificador API, nombre, fotografía) hacia columnas tangibles empleando SQLAlchemy.
- `templates/`: Abarca las formaciones visuales de cara a los clientes (`index.html` abarca la vista genérica e investigativa, y `favorites.html` administra las entidades persistidas correspondientes al usuario).

## Instrucciones de Instalación
1. Clona el repositorio actual dentro de tu unidad local.
2. (Opcional pero recomendable) Crea y activa un Entorno Virtual de Python.
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows de forma típica: .venv\Scripts\activate
   ```
3. Instala los paquetes y librerías pre-requisitos:
   ```bash
   pip install -r requirements.txt
   ```
4. Inicia la aplicación en forma. SQLAlchemy automáticamente conformará el archivo `.db` contenedor dentro de un sub-directorio de inicio llamado `instance` la primera vez que inicie.
   ```bash
   python app.py
   ```
5. Accede a tu navegador favorito dentro del puerto desplegado nativamente `http://127.0.0.1:5000/`.