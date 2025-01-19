from django.shortcuts import render, redirect
from django.http import HttpResponse


# Vista para manejar el login
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect

from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')
        station_code = request.POST.get('stationCode')

        # Rutas de los archivos de credenciales
        usuarios_file = 'mi_app/static/imagenes/credenciales.txt'  # Ruta del archivo de usuarios
        admin_file = 'mi_app/static/imagenes/administradores.txt'  # Ruta del archivo de administradores

        try:
            # Leer el archivo de usuarios
            with open(usuarios_file, 'r') as file:
                usuario_lines = file.readlines()

            # Leer el archivo de administradores
            with open(admin_file, 'r') as file:
                admin_lines = file.readlines()

            # Validar si las credenciales son de un administrador
            for line in admin_lines:
                stored_username, stored_password, stored_station_code = line.strip().split()
                if username == stored_username and password == stored_password and station_code == stored_station_code:
                    # Si las credenciales coinciden con un administrador
                    return redirect('HOME_ADMIN')  # Cambia por la URL de la página de administrador

            # Validar si las credenciales son de un usuario normal
            for line in usuario_lines:
                stored_username, stored_password, stored_station_code = line.strip().split()
                if username == stored_username and password == stored_password and station_code == stored_station_code:
                    # Si las credenciales coinciden con un usuario
                    return redirect('home')  # Cambia por la URL de la página de usuario

            # Si no se encuentra ninguna coincidencia
            return render(request, 'mi_app/login.html', {'error': 'Credenciales incorrectas'})

        except FileNotFoundError:
            # Manejo de error si no se puede encontrar el archivo de credenciales
            return render(request, 'mi_app/login.html', {'error': 'No se pudo acceder al archivo de credenciales'})

    # Si la solicitud no es POST, solo renderiza la página de login
    return render(request, 'mi_app/login.html')







from django.shortcuts import render
def home_view(request):
    return render(request, 'mi_app/home.html')  # Renderiza la página home

def subir_view(request):
    return render(request, 'mi_app/subir.html') #RENDERIZA SUBIR
def HOME_ADMIN(request):
    return render(request, 'mi_app/HOME_ADMIN.html')