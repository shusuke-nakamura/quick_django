from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(request):
    return HttpResponse('こんにちは、世界！')

def temp(request):
    context = {
        'msg': 'こんにちは、世界!'
    }
    return render(request, 'main/temp.html', context)

def list(request):
    books = Book.objects.all()
    return render(request, 'main/list.html', {
        'books': books
    })