from django.urls import path
from .views import Publicaciones

urlpatterns = [
    path('publicacion/<int:id>', Publicaciones, name='publicacion'),
    ]