from django.urls import path
from . import views

urlpatterns = [
    path('videos/', views.videos_list, name='videos_list'),
    path('videos/nuevo/', views.video_create, name='video_create'),
    path('usuarios/', views.usuarios_list, name='usuarios_list'),
    path('usuarios/nuevo/', views.usuario_create, name='usuario_create'),
    path('creditos/', views.creditos, name='creditos'),
]
