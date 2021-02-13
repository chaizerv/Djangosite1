from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def home(request):
    return render(request, 'main/home.html')

def egrul(request):
    return render(request, 'main/egrul.html')

def egrn(request):
    return render(request, 'main/egrn.html')

def i_egrul(request):
    return render(request, 'main/i_egrul.html')

def document(request):
    return render(request, 'main/document.html')

def ip(request):
    return render(request, 'main/ip.html')

def ooo(request):
    return render(request, 'main/ooo.html')

def spec(request):
    return render(request, 'main/spec.html')

def contact(request):
    return render(request, 'main/contact.html')