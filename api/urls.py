from django.urls import path
from .views import lista_categorias, lista_productos

urlpatterns = [
    path('categorias/', lista_categorias),
    path('productos/', lista_productos),
]