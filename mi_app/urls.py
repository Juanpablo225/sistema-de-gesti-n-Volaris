from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('subir/', views.subir_view, name='subir'),  # Cambié a views.subir_view
    path('HOME_ADMIN/', views.HOME_ADMIN, name='HOME_ADMIN'),
    path('combinar_archivos/', views.subir_view, name='combinar_archivos'),  # Cambié a views.subir_view
    path('descargar/<str:archivo>/', views.descargar_archivo, name='descargar_archivo'),
    path('subir_AD/', views.subir_AD, name='subir_AD'),




    path('users/', views.user_list_view, name='user_list'),  # Lista de usuarios
    path('users/delete/<int:user_id>/', views.delete_user_view, name='delete_user'),  # Eliminar usuario
    path('users/edit/<int:user_id>/', views.edit_user_view, name='edit_user'),  # Editar contraseña
]
