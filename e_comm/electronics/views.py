from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader

# Create your views here.
from .models import laptops


def index(request):
    return HttpResponse("hello Worlld")

def laptops_list(request):
    email = request.POST.get('email', 'testuser@example.com')
    password = request.POST.get('password', 'SECret.123')
    print(email, password)
    if email != password:
        return HttpResponseRedirect('/electronics/404')
    else:
        all_laptops = laptops.objects.all()
        laptop_dict = {}
        for i in all_laptops:
            laptop_dict[i.model] = i.name
        template = loader.get_template('laptop.html')

        context = {'laptop_dict': laptop_dict}

        return HttpResponse(template.render(context, request))

def get_laptops(request, no):
    all_laptops = laptops.objects.all()
    laptop_dict = {}
    for i in all_laptops:
        laptop_dict[i.model] = i.name

    if no in laptop_dict.keys():
        return HttpResponse("You request model : {}".format(laptop_dict[no]))
    else:
        return HttpResponse("Your requested model is not found. :(")
