"""
URL configuration for SIKIN project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Logro.views import CreateLogro, ListaAllLogros, ListaFeedLogros, EditarLogro, EliminarLogro, OcultarLogro
from Like.views import DarLikeView, EliminarLikeView, ListarLikesLogroView, ObtenerConteoLikesView



urlpatterns = [
    path('crear/', CreateLogro.as_view(), name='crear-logro'),
    path('listar-todos/', ListaAllLogros.as_view(), name='listar-todos-logros'),
    path('listar-feed/', ListaFeedLogros.as_view(), name='listar-feed-logros'),
    path('editar/<int:pk>/', EditarLogro.as_view(), name='editar-logro'),
    path('eliminar/<int:pk>/', EliminarLogro.as_view(), name='eliminar-logro'),
    path('ocultar/<int:pk>/', OcultarLogro.as_view(), name='ocultar-logro'),


    path('dar_like/<int:pk>/', DarLikeView.as_view(), name='dar_like'),
    path('eliminar_like/<int:pk>/', EliminarLikeView.as_view(), name='eliminar_like'),
    path('listar_likes_logro/<int:pk>/', ListarLikesLogroView.as_view(), name='listar_likes_logro'),
    path('obtener_conteo_likes/<int:pk>/', ObtenerConteoLikesView.as_view(), name='obtener_conteo_likes'),

]

