# biblioteca_publica

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

Crear y activar entorno virtual:

python manage.py makemigrations
python manage.py migrate

Instalar dependencias:

pip install -r requirements.txt

Aplicar migraciones:python manage.py makemigrations
python manage.py migrate


🚀 Ejecutar el servidor

python manage.py runserver


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


