from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blogs
from .forms import blogForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def inicio(request):
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def blogs(request):
    blogs=Blogs.objects.all()
    return render(request, 'blogs/index.html', {'blogs':blogs})

def crear(request):
    formulario=blogForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('blogs')
    return render(request, 'blogs/crear.html', {'formulario':formulario})   

def editar(request, id):
    blog=Blogs.objects.get(id=id)
    formulario=blogForm(request.POST or None, request.FILES or None, instance=blog)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('blogs')
    return render(request, 'blogs/editar.html', {'fortmulario':formulario})

def borrar(request,id):
    blog=Blogs.objects.get(id=id)
    blog.delete()
    blogs=Blogs.objects.all()
    contexto={'blogs':blogs}
    return render(request,'blogs/form.html', contexto)

def login(request):
    if request.method == 'POST':
        form=AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            user=authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request, 'paginas/inicio.html', {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, 'paginas/inicio.html', {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request,'paginas/inicio.html', {"mensaje":"Error, formulario erroneo"})
    form= AuthenticationForm()
    return render(request, 'paginas/login.html', {'form':form})

def registro(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request, 'paginas/inicio.html', {"mensaje":"Usuario Creado"})
        else:
            form=UserCreationForm
        return render(request, 'paginas/inicio.html', {'form':form})  

