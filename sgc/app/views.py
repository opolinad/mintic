from django.shortcuts import render
from django.http import JsonResponse
from .models import Usuario, Proyecto
from django.shortcuts import redirect,reverse

# Create your views here.

def main (request):
    return render(request, 'index.html')

def login (request):
    return render(request, 'login.html')

def home_admin (request):
    return render(request, 'home-admin.html')

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
                if usuario.tUsuario == "estudiante":
                    return redirect("/home-estudiante")
            else:
                return redirect("/login?valid=false")
        except:
            return redirect("/login?valid=false")

def projects_api (request, id=None):
    try:
        if request.method == "GET" and id!=None:
            return JsonResponse({'proyecto':list(Proyecto.objects.filter(id=id).values())})

        elif request.method == "GET":
            return JsonResponse({'proyectos':Proyecto.objects.all().values()})

        elif request.method == "POST" and request.POST.get('_method') == "PUT":
            project = Proyecto.objects.filter(id=id).update(nombre=request.POST.get('nombre'), estado =request.POST.get('estado') )
            return JsonResponse({'msg':"Actulizado"})

        elif request.method == "POST" and request.POST.get('_method') == "DELETE":
            Proyecto.objects.filter(id=id).delete()
            return JsonResponse({'msg':"Borrado"})

        elif request.method == "POST":
            project = Proyecto.objects.create(nombre=request.POST.get('nombre'), estado =request.POST.get('estado') )
            return JsonResponse({'msg':"Creado"})
    except:
        return JsonResponse({'msg':"Error"})

def users_api (request, id=None):
    try:
        if request.method == "GET" and id!=None:
            return JsonResponse({'usuario':list(Usuario.objects.filter(id=id).values())})

        elif request.method == "GET":
            return JsonResponse({'usuarios':Usuario.objects.all().values()})

        elif request.method == "POST" and request.POST.get('_method') == "PUT":
            user = Usuario.objects.filter(id=id).update(
                tipoIdentificado = request.POST.get('tipoIdentificado'),
                tUsuario = request.POST.get('tUsuario'),
                clave = request.POST.get('clave'),
                nombre = request.POST.get('nombre'),
                apellidos = request.POST.get('apellidos'),
                telefono = request.POST.get('telefono'),
                genero = request.POST.get('genero'),
                estado = request.POST.get('estado'),
                idProyecto = request.POST.get('idProyecto'),
                notaDefinitivaProyecto = request.POST.get('notaDefinitivaProyecto')
            )
            return JsonResponse({'msg':"Actulizado"})

        elif request.method == "POST" and request.POST.get('_method') == "DELETE":
            Usuario.objects.filter(id=id).delete()
            return JsonResponse({'msg':"Borrado"})

        elif request.method == "POST":
            user = Usuario.objects.create(tipoIdentificado=request.POST.get('tipoIdentificado'),
                tUsuario =request.POST.get('tUsuario'),
                clave =request.POST.get('clave'),
                nombre =request.POST.get('nombre'),
                apellidos =request.POST.get('apellidos'),
                telefono =request.POST.get('telefono'),
                genero =request.POST.get('genero'),
                estado =request.POST.get('estado'),
                idProyecto =request.POST.get('idProyecto'),
                notaDefinitivaProyecto =request.POST.get('notaDefinitivaProyecto')
            )
            return JsonResponse({'msg':"Creado"})
    except:
        return JsonResponse({'msg':"Error"})