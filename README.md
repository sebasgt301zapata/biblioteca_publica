# Biblioteca Pública

Este es un proyecto web de gestión de biblioteca desarrollado con **Django 4.2**.  
Permite visualizar un catálogo de libros, filtrarlos por categoría, seleccionar libros para préstamo y confirmar préstamos reales con almacenamiento en base de datos.

---

## 📂 Funcionalidades

### 📚 Catálogo de Libros
- Lista de todos los libros registrados
- Visualización de título, autor, categoría y año
- Filtro por categoría

### ➕ Selección de Préstamo
- Agregar libros a una selección (carrito)
- Ver selección actual
- Quitar libros de la selección

### 📌 Confirmar Préstamo
- Guarda préstamos en la base de datos
- Crea préstamo real con todos los libros seleccionados

### 👤 Modelos Implementados
- `Book` – libros del catálogo
- `Category` – categorías o géneros de libros
- `Reader` – lector que realiza préstamos
- `Loan` – préstamo realizado por un lector
- `LoanItem` – detalle de cada préstamo

---

## 🧠 Requisitos

- Python 3.9 o superior
- Django 4.2
- VirtualEnv

---

## 🛠️ Instalación
git clone https://github.com/sebasgt301zapata/biblioteca_publica
-cd biblioteca_publica


##Crear y activar entorno virtual:

-python -m venv venv

##Windows:

-venv\Scripts\activate

##Linux / macOS:

source venv/bin/activate


##Instalar dependencias:

-pip install -r requirements.txt


##Aplicar migraciones:

-python manage.py makemigrations

-python manage.py migrate


##🚀 Ejecutar el servidor

-python manage.py runserver

##Abrir en el navegador:

http://127.0.0.1:8000/

🏗️ Arquitectura del Proyecto

El proyecto sigue una arquitectura basada en MVC (Modelo – Vista – Template) utilizando Django.

📦 Componentes principales
🔹 Modelos

Book: Representa un libro (título, autor, año, categoría)

Category: Clasificación de los libros

Reader: Persona que realiza préstamos

Loan: Préstamo realizado por un lector

LoanItem: Relación entre préstamo y libros

🔹 Dominio

LoanSelection: Maneja la selección temporal de libros usando sesiones (carrito de préstamo)

LoanSelectionItem: Representa un libro dentro de la selección

🔹 Vistas

BookListView (CBV): Muestra el catálogo de libros

add_to_selection: Agrega libros a la selección

selection_detail: Muestra la selección actual

remove_from_selection: Elimina libros de la selección

confirm_loan: Confirma el préstamo y lo guarda en la base de datos

🔹 Templates

Interfaz completamente en español

Uso de HTML + CSS

Navegación clara entre catálogo, selección y confirmación

🔄 Flujo de Uso

1️⃣ El usuario ingresa al catálogo de libros
2️⃣ Selecciona uno o más libros
3️⃣ Visualiza la selección de préstamo
4️⃣ Puede quitar libros si lo desea
5️⃣ Confirma el préstamo
6️⃣ El sistema:

Crea el préstamo

Asocia los libros

Limpia la selección

Muestra confirmación

Flujo resumido:

Catálogo → Agregar libro → Ver selección → Confirmar préstamo → Préstamo creado

🗂️ Estructura del Proyecto – Biblioteca Pública
```bash

biblioteca_publica/
│
├── manage.py
│
├── biblioteca_publica/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── library/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── selection.py
│   ├── migrations/
│   │   └── __init__.py
│   │
│   ├── templates/
│   │   └── library/
│   │       ├── book_list.html
│   │       ├── book_form.html
│   │       ├── book_confirm_delete.html
│   │       ├── category_form.html
│   │       ├── category_confirm_delete.html
│   │       ├── selection_detail.html
│   │       └── loan_confirmed.html
│   │
│   └── static/
│       └── library/
│           └── styles.css
│
└── venv/





