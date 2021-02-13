from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles


def index(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

