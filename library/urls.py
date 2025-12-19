from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),

    path('seleccion/', views.selection_detail, name='selection_detail'),
    path('seleccion/agregar/<int:book_id>/', views.add_to_selection, name='add_to_selection'),
    path('seleccion/quitar/<int:book_id>/', views.remove_from_selection, name='remove_from_selection'),
    path('seleccion/confirmar/', views.confirm_loan, name='confirm_loan'),
]


