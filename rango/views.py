from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context_dict = {'boldmessage': 'crispy, tenderness'}
    return render(request,'rango/index.html',context=context_dict )

def about(request):
    return HttpResponse("This is where my about page will go")
    