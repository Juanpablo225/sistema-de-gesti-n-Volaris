from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
import os
from django.conf import settings


from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.auth import authenticate, login



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:  # Si es superusuario (admin)
                return redirect('HOME_ADMIN')
            else:
                return redirect('home')
        else:
            return render(request, 'mi_app/login.html', {'error': 'Credenciales incorrectas'})

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













# Vista para listar usuarios
def user_list_view(request):
    users = User.objects.all()  # Obtener todos los usuarios
    return render(request, 'mi_app/user_list.html', {'users': users})

# Vista para eliminar un usuario
def delete_user_view(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return redirect('user_list')  # Redirige de nuevo a la lista de usuarios
    except User.DoesNotExist:
        return redirect('user_list', {'error': 'Usuario no encontrado'})

# Vista para editar la contraseña de un usuario
def edit_user_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = PasswordChangeForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Mantener la sesión activa
            return redirect('user_list')  # Redirigir a la lista de usuarios
        else:
            return render(request, 'mi_app/edit_user.html', {'form': form, 'user': user, 'error': 'Contraseña no válida'})
    else:
        form = PasswordChangeForm(user=user)
    return render(request, 'mi_app/edit_user.html', {'form': form, 'user': user})