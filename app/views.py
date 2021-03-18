from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    article = Article.objects.all()
    return render(request, 'index.html', locals())

def content(request):
    content = Content.objects.all()
    return render(request, 'content.html', locals())

def test(request):
    return render(request, 'test.html')
