from django.shortcuts import render
from random import randint
# Create your views here.

def kviz(request):
    pla = randint(0,30)
    plb = randint(0,30)
    fela = randint(0,30)
    felb = randint(0,30)
    plmo = titkos_fuggveny(pla,plb)
    template = "kviz.html"
    context = {
        'pla':pla, 
        'plb':plb, 
        'plmo':plmo,
        'fela':fela,
        'felb':felb,
        'volt_valasz': request.method!="GET",
    }

    if request.method=="POST":
        regifela = int(request.POST['regifela'])
        regifelb = int(request.POST['regifelb'])
        regifelmo_user_szerint = int(request.POST['felmo'])
        regifelmo_valojaban = titkos_fuggveny(regifela, regifelb)

        # print(regifela)
        # print(regifelb)
        # print(regifelmo_user_szerint)
        # print(regifelmo_valojaban)

        context['helyes'] = regifelmo_user_szerint == regifelmo_valojaban

    return render(request, template, context)


def titkos_fuggveny(a,b):
    return 2*a+b
