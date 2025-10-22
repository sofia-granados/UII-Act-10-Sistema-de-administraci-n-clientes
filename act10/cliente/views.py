from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Cliente
from .forms import ClienteForm

def index(request):
    return render(request, 'cliente/index.html', {
        'clientes': Cliente.objects.all().order_by('-id')
    })

def view_cliente(request, id):
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        print("=== DEPURACIÓN ADD ===")
        print("Formulario válido:", form.is_valid())
        
        if form.is_valid():
            cliente = form.save()
            print(f"Cliente guardado: {cliente.nombre} {cliente.apepaterno} (ID: {cliente.id})")
            # Redirige DIRECTAMENTE a la lista
            return HttpResponseRedirect(reverse('index'))
        else:
            print("Errores del formulario:", form.errors)
    else:
        form = ClienteForm()
    
    return render(request, 'cliente/add.html', {
        'form': form
    })

def edit(request, id):
    if request.method == 'POST':
        cliente = Cliente.objects.get(pk=id)
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        cliente = Cliente.objects.get(pk=id)
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente/edit.html', {
        'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        cliente = Cliente.objects.get(pk=id)
        cliente.delete()
    return HttpResponseRedirect(reverse('index'))