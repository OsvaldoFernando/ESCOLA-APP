from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Sistema Aberto com Django</h1><p>O sistema foi migrado para Django com sucesso.</p>')
