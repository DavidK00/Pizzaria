from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Pizza, Toppings


# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')

def pizza(request):
    pizzas = Pizza.objects.all()
    template = loader.get_template('MainApp/list.html')
    context = {'pizzas':pizzas}
    return HttpResponse(template.render(context, request))

def indiv_pizza(request, pizza_id):
    indiv_pizza = Pizza.objects.get(id = pizza_id)
    toppings = Toppings.toppings_set()
    template = loader.get_template('MainApp/pizza.html')
    context = {'indiv_pizza':indiv_pizza, "toppings": toppings}
    return HttpResponse(template.render(context, request))







    

    