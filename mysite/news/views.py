from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request, 'news/news_home.html')

