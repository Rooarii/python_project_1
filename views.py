from django.shortcuts import render
'''
# Create your views here.

def index(request):
    return render(request,'myapp/index.html')'''
import datetime
from .dictionnaires import Article

def index(request):
    today = datetime.datetime.now().date()
    filtre = 'Joel est une limace limace'
    jourSem = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']
    return render(request, 'myapp/index.html',{'today': today, 'filtre': filtre, 'jourSem': jourSem})

def list(request):
    Articles = Article.all()
    print(Articles)
    return render(request, 'myapp/list.html', {'Articles':  Articles})

def details(request, id):
    article = Article.find(id)
    return render(request, 'myapp/details.html', {'Article' : article})