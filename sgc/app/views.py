from django.shortcuts import render
from django.http import JsonResponse
from .models import Usuario
from django.shortcuts import redirect,reverse

# Create your views here.

def main (request):
    return redirect("/login")

def login (request):
    return render(request, 'login.html')

def home_admin (request):
    return render(request, 'index2yt.html')

def home_proffesor (request):
    return render(request, 'home-profesor.html')

def home_student (request):
    return render(request, 'home-estudiante.html')

def login_api (request):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            usuario = Usuario.objects.get(correo=email)
            if usuario.clave == password:
                if usuario.tUsuario == "admin":
                    return redirect("/home-admin")
                if usuario.tUsuario == "profesor":
                    return redirect("/home-profesor")
                if usuario.tUsuario == "estudiante":
                    return redirect("/home-estudiante")
            else:
                return redirect("/login?valid=false")
        except:
            return redirect("/login?valid=false")