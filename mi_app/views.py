from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
import os
from django.conf import settings


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


def home_view(request):
    return render(request, 'mi_app/home.html')  # Renderiza la página home

def HOME_ADMIN(request):
    return render(request, 'mi_app/HOME_ADMIN.html')



def subir_view(request):
    archivo_combinado = None

    if request.method == 'POST':
        archivo1 = request.FILES.get('archivo1')
        archivo2 = request.FILES.get('archivo2')

        # Lógica para combinar los archivos (Este es solo un ejemplo básico)
        if archivo1 and archivo2:
            # Crear un archivo combinado (en este caso simplemente los concatenamos)
            archivo_combinado = 'archivo_combinado.pdf'  # Cambia el nombre de archivo si lo necesitas

            # Guardar el archivo combinado en el directorio 'media'
            with open(os.path.join(settings.MEDIA_ROOT, archivo_combinado), 'wb') as f:
                for archivo in [archivo1, archivo2]:
                    for chunk in archivo.chunks():
                        f.write(chunk)

            # Retornar al template con el nombre del archivo combinado
            return render(request, 'mi_app/subir.html', {
                'archivo_combinado': archivo_combinado
            })

    # Si no se han subido archivos o no es un POST, renderiza el formulario vacío
    return render(request, 'mi_app/subir.html', {'archivo_combinado': archivo_combinado})



def subir_AD(request):
    archivo_combinado = None

    if request.method == 'POST':
        archivo1 = request.FILES.get('archivo1')
        archivo2 = request.FILES.get('archivo2')

        # Lógica para combinar los archivos (Este es solo un ejemplo básico)
        if archivo1 and archivo2:
            # Crear un archivo combinado (en este caso simplemente los concatenamos)
            archivo_combinado = 'archivo_combinado.pdf'  # Cambia el nombre de archivo si lo necesitas

            # Guardar el archivo combinado en el directorio 'media'
            with open(os.path.join(settings.MEDIA_ROOT, archivo_combinado), 'wb') as f:
                for archivo in [archivo1, archivo2]:
                    for chunk in archivo.chunks():
                        f.write(chunk)

            # Retornar al template con el nombre del archivo combinado
            return render(request, 'mi_app/subir.html', {
                'archivo_combinado': archivo_combinado
            })

    # Si no se han subido archivos o no es un POST, renderiza el formulario vacío
    return render(request, 'mi_app/subir_AD.html', {'archivo_combinado': archivo_combinado})















def descargar_archivo(request, archivo):
    archivo_path = os.path.join(settings.MEDIA_ROOT, archivo)

    # Verifica si el archivo existe
    if os.path.exists(archivo_path):
        return FileResponse(open(archivo_path, 'rb'), as_attachment=True, filename=archivo)

    return HttpResponse('Archivo no encontrado', status=404)
