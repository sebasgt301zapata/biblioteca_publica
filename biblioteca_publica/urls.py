from django.contrib import admin
from django.urls import path, include
from django.urls import path
from library.views import (
    BookListView,
    BookCreateView,
    BookDeleteView,
    CategoryCreateView,
    CategoryDeleteView,
    add_to_selection,
    remove_from_selection,
    selection_detail,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BookListView.as_view(), name='book_list'),

    path('categorias/nueva/', CategoryCreateView.as_view(), name='category_create'),
    path('categorias/eliminar/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    path('libros/nuevo/', BookCreateView.as_view(), name='book_create'),
    path('libros/eliminar/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),

    path('seleccion/', selection_detail, name='selection_detail'),
    path('seleccion/agregar/<int:book_id>/', add_to_selection, name='add_to_selection'),
    path('seleccion/eliminar/<int:book_id>/', remove_from_selection, name='remove_from_selection'),
    path('admin/', admin.site.urls),
    path('', include('library.urls')),
]
