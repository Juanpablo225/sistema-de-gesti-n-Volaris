from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('subir/', views.login_view, name='subir'),
path('HOME_ADMIN/', views.HOME_ADMIN, name='HOME_ADMIN'),
]
