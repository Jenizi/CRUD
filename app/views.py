from django.shortcuts import render, redirect
from django.contrib import messages
from app.forms import LabForm
from app.models import Lab


def home(request):
    data = {}
    data['db'] = Lab.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = LabForm()
    return render(request, 'form.html', data)


def create(request):
    form = LabForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Criado com sucesso!')
        return redirect("home")

    return render(request, 'form.html', {'form': form})


def view(request, pk):
    data = {}
    data['db'] = Lab.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    lab = Lab.objects.get(pk=pk)
    form = LabForm(request.POST or None, instance=lab)
    if form.is_valid():
        form.save()
        print('aqui')
        return redirect("home")
    return render(request, 'form.html', {'db': lab, 'form': form})


def update(request, pk):
    data = {}
    data['db'] = Lab.objects.get(pk=pk)
    form = LabForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        messages.success(request, 'Editado com sucesso!')
    return redirect('home')


def delete(request, pk):
    db = Lab.objects.get(pk=pk)
    db.delete()
    return redirect('home')
