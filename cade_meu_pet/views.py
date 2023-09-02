from django.shortcuts import render, redirect
from .models import AnimalEncontrado, AnimalPerdido
from .forms import AnimalEncontradoForm, AnimalPerdidoForm
from datetime import datetime


def index(request):
    animais_perdidos = AnimalPerdido.objects.all()
    animais_encontrados = AnimalEncontrado.objects.all()
    context = {
        'animais_perdidos': animais_perdidos,
        'animais_encontrados': animais_encontrados
    }
    return render(request, 'index.html', context)

def perdidos(request):
    if request.method == 'POST':
        form = AnimalPerdidoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                animal_perdido = form.save(commit=False)
                animal_perdido.save()
                return redirect('envio_sucesso')
            except Exception as e:
                print(form.errors)  # Imprime os erros do formulário para depuração
                return redirect('form_error')  # Redireciona para a página de erro
        else:
            print(form.errors)  # Imprime os erros do formulário para depuração
            return redirect('form_error')  # Redireciona para a página de erro
    else:
        form = AnimalPerdidoForm()
    context = {'form': form}
    return render(request, 'perdidos.html', context)


def encontrados(request):
    if request.method == 'POST':
        form = AnimalEncontradoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                animal_encontrado = form.save(commit=False)
                nome = form.cleaned_data.get('nome')
                raca = form.cleaned_data.get('raca')

                # Define "não informado" como valor padrão se o campo estiver vazio
                if not nome:
                    animal_encontrado.nome = 'não informado'
                if not raca:
                    animal_encontrado.raca = 'não informado'

                animal_encontrado.save()
                return redirect('envio_sucesso')
            except Exception as e:
                print(form.errors)  # Imprime os erros do formulário para depuração
                return redirect('form_error')  # Redireciona para a página de erro
        else:
            print(form.errors)  # Imprime os erros do formulário para depuração
            return redirect('form_error')  # Redireciona para a página de erro
    else:
        form = AnimalEncontradoForm()
    context = {'form': form}
    return render(request, 'encontrados.html', context)
    
def lista_encontrados(request):
    animais_encontrados = AnimalEncontrado.objects.all()

    especies = AnimalEncontrado.objects.values_list('especie', flat=True).distinct()
    racas = AnimalEncontrado.objects.values_list('raca', flat=True).distinct()
    cores = AnimalEncontrado.objects.values_list('cor', flat=True).distinct()
    datas = AnimalEncontrado.objects.values_list('data_encontrado', flat=True).distinct()
    locais = AnimalEncontrado.objects.values_list('local_encontrado', flat=True).distinct()

    especie_filtro = request.GET.get('especie')
    raca_filtro = request.GET.get('raca')
    cor_filtro = request.GET.get('cor')
    data_filtro = request.GET.get('data')
    local_filtro = request.GET.get('local')

    if especie_filtro:
        animais_encontrados = animais_encontrados.filter(especie=especie_filtro)
    if raca_filtro:
        animais_encontrados = animais_encontrados.filter(raca=raca_filtro)
    if cor_filtro:
        animais_encontrados = animais_encontrados.filter(cor=cor_filtro)
    if data_filtro:
        # Converter a data para o formato YYYY-MM-DD
        data_filtro = datetime.strptime(data_filtro, "%B %d, %Y").strftime("%Y-%m-%d")
        animais_encontrados = animais_encontrados.filter(data_encontrado=data_filtro)
    if local_filtro:
        animais_encontrados = animais_encontrados.filter(local_encontrado=local_filtro)

    context = {
        'animais_encontrados': animais_encontrados,
        'especies': especies,
        'racas': racas,
        'cores': cores,
        'datas': datas,
        'locais': locais,
        'especie_filtro': especie_filtro,
        'raca_filtro': raca_filtro,
        'cor_filtro': cor_filtro,
        'data_filtro': data_filtro,
        'local_filtro': local_filtro
    }

    return render(request, 'lista_encontrados.html', context)

def lista_perdidos(request):
    animais_perdidos = AnimalPerdido.objects.all()

    especies = AnimalPerdido.objects.values_list('especie', flat=True).distinct()
    racas = AnimalPerdido.objects.values_list('raca', flat=True).distinct()
    cores = AnimalPerdido.objects.values_list('cor', flat=True).distinct()
    datas = AnimalPerdido.objects.values_list('data_perdido', flat=True).distinct()
    locais = AnimalPerdido.objects.values_list('local_perdido', flat=True).distinct()

    especie_filtro = request.GET.get('especie')
    raca_filtro = request.GET.get('raca')
    cor_filtro = request.GET.get('cor')
    data_filtro = request.GET.get('data')
    local_filtro = request.GET.get('local')

    if especie_filtro:
        animais_perdidos = animais_perdidos.filter(especie=especie_filtro)
    if raca_filtro:
        animais_perdidos = animais_perdidos.filter(raca=raca_filtro)
    if cor_filtro:
        animais_perdidos = animais_perdidos.filter(cor=cor_filtro)
    if data_filtro:
        # Converter a data para o formato YYYY-MM-DD
        data_filtro = datetime.strptime(data_filtro, "%B %d, %Y").strftime("%Y-%m-%d")
        animais_perdidos = animais_perdidos.filter(data_perdido=data_filtro)
    if local_filtro:
        animais_perdidos = animais_perdidos.filter(local_perdido=local_filtro)

    context = {
        'animais_perdidos': animais_perdidos,
        'especies': especies,
        'racas': racas,
        'cores': cores,
        'datas': datas,
        'locais': locais,
        'especie_filtro': especie_filtro,
        'raca_filtro': raca_filtro,
        'cor_filtro': cor_filtro,
        'data_filtro': data_filtro,
        'local_filtro': local_filtro
    }

    return render(request, 'lista_perdidos.html', context)
    
def envio_sucesso(request):
    return render(request, 'envio_sucesso.html')

def form_error(request):
    return render(request, 'form_error.html')
