from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context_dict = {'boldmessage': "Bold Message!"}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'boldmessage': "About Bold Message!"}
    return render(request, 'about/index.html', context_dict)