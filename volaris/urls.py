
from django.contrib import admin
from django.urls import path, include
from mi_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.login_view, name='login'), # Redirige la raíz al login

path('home/', views.home_view, name='home'),
    path('subir/', views.subir_view, name='subir'),
path('HOME_ADMIN/', views.HOME_ADMIN, name='HOME_ADMIN'),

path('subir_AD/', views.subir_AD, name='subir_AD'),

    path('users/', views.user_list_view, name='user_list'),  # Lista de usuarios
    path('users/delete/<int:user_id>/', views.delete_user_view, name='delete_user'),  # Eliminar usuario
    path('users/edit/<int:user_id>/', views.edit_user_view, name='edit_user'),  # Editar contraseña


]

