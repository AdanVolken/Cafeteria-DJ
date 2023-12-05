from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render, get_object_or_404
from .models import Bebida,Comida
from .forms import FormularioBebidas,FormularioComida
# Create your views here.

def home(request):
    comida = Comida.objects.all()
    bebida = Bebida.objects.all()
    return render(request, "home.html", {
        "comida": comida,
        "bebida":bebida,
    })

def bebida(request):
    # Filtrar las bebidas disponibles
    bebidas_disponibles = Bebida.objects.filter(disponible=True)

    # Dividir las bebidas en dos conjuntos: normales y alcohólicas
    bebidas_normales = bebidas_disponibles.filter(alcohol=False)
    bebidas_alcoholicas = bebidas_disponibles.filter(alcohol=True)

    return render(request, "bebida.html", {
        'normales': bebidas_normales,
        'alcoholicas': bebidas_alcoholicas,
        'bebidas': bebidas_disponibles,
    })

def comida(request):
    # Filtrar las bebidas disponibles
    comidas_disponibles = Comida.objects.filter(disponible=True)

    # Dividir las bebidas en dos conjuntos: normales y alcohólicas
    comida = comidas_disponibles.all()

    return render(request, "comida.html", {
        'comidas': comida,
        'comidas_disponibles': comidas_disponibles,
    })
#Login
def inicio_sesion(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm()
        })
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error' : 'Usuario o contraseña Incorrecta'
            })

        else:
            login(request, user)
            return redirect('productos')



def productos(request):
        return render(request, 'productos.html', {
            'comidas': Comida.objects.all(),  
            'bebidas': Bebida.objects.all(),  
            'form_comida': FormularioComida,
            'form_bebida': FormularioBebidas,
        })
 
################################################################################################################################
#AGREGAR PRODUCTOS
################################################################################################################################

def agregar_comida(request):
    if request.method == 'GET':
        return render(request, 'productos.html', {
            'form_comida': FormularioComida,
        })
    else:
        form_comida = FormularioComida(request.POST,request.FILES)
        if form_comida.is_valid():
            nombre_c = form_comida.cleaned_data['nombre']
            descripcion_c = form_comida.cleaned_data['ingredientes']
            precio_c = form_comida.cleaned_data['precio']
            imagen_c = form_comida.cleaned_data['imagen']
            disponible_c = form_comida.cleaned_data['disponible']

            nueva_comida = Comida(nombre=nombre_c, ingredientes=descripcion_c, precio=precio_c, imagen=imagen_c, disponible= disponible_c)
            nueva_comida.save()

            return redirect('productos')


def agregar_bebida(request):
    if request.method == 'GET':
        return render(request, 'productos.html',{
            'form_comida': FormularioBebidas,
        })
    else:
            form_bebida = FormularioBebidas(request.POST,request.FILES)
            if form_bebida.is_valid():
                nombre_b = form_bebida.cleaned_data['nombre']
                descripcion_b = form_bebida.cleaned_data['ingredientes']
                precio_b = form_bebida.cleaned_data['precio']
                imagen_b = form_bebida.cleaned_data['imagen']
                alcohol = form_bebida.cleaned_data['alcohol']
                disponible_b = form_bebida.cleaned_data['disponible']

                nueva_bebida = Bebida(nombre=nombre_b, ingredientes=descripcion_b, precio=precio_b, imagen=imagen_b, alcohol=alcohol , disponible = disponible_b)
                nueva_bebida.save()

                return redirect('productos')

################################################################################################################################
# BOTONES DE EDICION
################################################################################################################################


def editar_bebida(request, id_bebida):
    if request.method == 'GET':
        bebida = Bebida.objects.get(id=id_bebida)
        form_b = FormularioBebidas(instance=bebida)
        return render(request, 'editar_comida.html', {
            'form_b': form_b,
            'bebida': bebida
         })
    else:
        bebida = Bebida.objects.get(id=id_bebida)
        form_b = FormularioBebidas(request.POST, instance=bebida)
        if form_b.is_valid():
            form_b.save()
            return redirect('productos')
        
def editar_comida(request, id_comida):
    if request.method == 'GET':
        comida = Comida.objects.get(id=id_comida)
        form_c = FormularioComida(instance=comida)
        return render(request, 'editar_comida.html', {
            'form_c': form_c,
            'comida': comida
         })
    else:
        comida = Comida.objects.get(id=id_comida)
        form_c = FormularioComida(request.POST, instance=comida)
        if form_c.is_valid():
            form_c.save()
            return redirect('productos')

#################################################################################################################################       
# BOTONES PARA ELIMINAR
################################################################################################################################

def eliminar_bebida(request, id_bebida):
    bebida = get_object_or_404(Bebida,id=id_bebida)
    bebida.delete()
    return redirect('productos')


def eliminar_comida(request, id_comida):
    comida = get_object_or_404(Comida, id=id_comida)
    comida.delete()
    return redirect('productos')