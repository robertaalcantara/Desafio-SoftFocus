from django.shortcuts import render, redirect
from .models import Comunicacao
from django.db.models import Q
from .forms import ComunicacaoForm
from django.contrib import messages
from haversine import haversine

verifica_veracidade = True

def list_comunicacoes(request):
    comunicacoes = Comunicacao.objects.all()

    busca = request.GET.get('busca')

    if busca:
        comunicacoes = Comunicacao.objects.filter(cpf_produtor__icontains = busca)

    return render(request, 'comunicacoes.html', {'comunicacoes': comunicacoes})


def create_comunicacao(request):
    form = ComunicacaoForm(request.POST or None)

    if form.is_valid():

        dados = form.data
        global verifica_veracidade

        nome_form = dados.__getitem__('nome_produtor')
        cpf_form = dados.__getitem__('cpf_produtor')
        email_form = dados.__getitem__('email_produtor')
        lat_form = float(dados.__getitem__('latitude_lavoura'))
        long_form = float(dados.__getitem__('longitude_lavoura'))
        evento_form = dados.__getitem__('evento')
        data_form = dados.__getitem__('data_colheita')

        #validar CPF

        if verifica_veracidade:

            coord_forms = (lat_form, long_form)
            comunicacoes = Comunicacao.objects.filter(Q(data_colheita =data_form) & ~Q(evento = evento_form))

            if comunicacoes:
                for comunicacao in comunicacoes:
                    print(comunicacao)
                    coord_banco = (comunicacao.latitude_lavoura, comunicacao.longitude_lavoura)

                    distancia = haversine(coord_banco, coord_forms)
                    print(distancia)

                    if distancia < 10 and verifica_veracidade == True:
                        messages.warning(request, f'ATENÇÃO: Na data {data_form}, há dois eventos divergentes com distância superior a 10 km entre eles. \n Já se encontra cadastrado o evento {comunicacao.evento} e está sendo inserido o evento {evento_form}.\n Ao clicar em salvar você está concordando com a veracidade deste fato!')
                        verifica_veracidade = False
                        break       
                    else:
                        form.save()
                        verifica_veracidade = True
                        return redirect('list_comunicacoes')

            else:
                form.save()
                verifica_veracidade = True
                return redirect('list_comunicacoes')  
        else:
            verifica_veracidade = True
            form.save()
            return redirect('list_comunicacoes')       

    return render(request, 'comunicacoes-form.html', {'form': form})
   
def update_comunicacao(request, id):
    comunicacao = Comunicacao.objects.get(id=id)
    form = ComunicacaoForm(request.POST or None, instance=comunicacao)

    if form.is_valid():
        form.save()
        return redirect('list_comunicacoes')

    return render(request, 'comunicacoes-form.html', {'form': form, 'comunicacao': comunicacao})

def delete_comunicacao(request, id):
    comunicacao = Comunicacao.objects.get(id=id)

    if request.method == 'POST':
        comunicacao.delete()
        return redirect('list_comunicacoes')

    return render(request, 'comunicacao-delete.html', {'comunicacao': comunicacao})
