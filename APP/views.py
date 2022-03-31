from django.shortcuts import render
from random import randint
# Create your views here.

def kviz(request):
    pla = randint(0,30)
    plb = randint(0,30)
    plmo = titkos_fuggveny(pla,plb)
    template = "kviz.html"
    context = {
        'pla':pla, 
        'plb': plb, 
        'plmo':plmo,
        'fela':randint(0,30),
        'felb':randint(0,30),
    }

    if request.method=="POST":
        print(int(request.POST['regifela']))
        print(int(request.POST['regifelb']))
        print(int(request.POST['felmo']))
        print(titkos_fuggveny(int(request.POST['regifela']), int(request.POST['regifelb']))==int(request.POST['felmo']))
    return render(request, template, context)


def titkos_fuggveny(a,b):
    return 2*a+b
