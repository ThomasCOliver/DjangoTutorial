from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context = {"phrase": "This is the phrase"}
    return render(request, 'index.html', context)