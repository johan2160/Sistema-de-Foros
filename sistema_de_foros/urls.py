from django.contrib import admin
from django.urls import path
from foros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mostrarIndex),
    path('login/', views.mostrarLogin),
    path('signup/', views.mostrarSignup),
    path('perfil_usuario/', views.mostrarPerfilUsuario),
    path('editar_perfil_usuario/', views.mostrarEditarPerfilUsuario),
    path('foro/', views.mostrarForo),
    path('foro/crear_comentario/', views.mostrarCrearComentario),
    path('foro/editar_comentario/', views.mostrarEditarComentario),
    path('crear_foro/', views.mostrarCrearForo),
    path('editar_foro/', views.mostrarEditarForo),
    path('crear_tematica/', views.mostrarCrearTematica),
    path('editar_tematica/', views.mostrarEditarTematica),
    path('gestionar_usuario/', views.mostrarGestionarUsuario),
    path('historial_acciones/', views.mostrarHistorialAcciones),
]
