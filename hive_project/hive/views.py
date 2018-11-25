from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse

posts = [
    {
        'author': 'toto',
        'title': 'hive Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'titi',
        'title': 'hive Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

# Create your views here. each def, represents a view with a pattern model inside to apply on it

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')