from django.shortcuts import render


def index(request):
    data = {'title': 'Сигирия - Юридические услуги',
            'values': '1',
            'value': '3',

    }
    return render(request, 'main/index.html', data)

def home(request):
    return render(request, 'main/home.html', {'title': 'О нас'})

def egrul(request):
    return render(request, 'main/egrul.html', {'title': 'Выписки из ЕГРЮЛ'})

def egrn(request):
    return render(request, 'main/egrn.html', {'title': 'Выписки из ЕГРН'})

def i_egrul(request):
    return render(request, 'main/i_egrul.html', {'title': 'Внесение изменений в ЕГРЮЛ'})

def document(request):
    return render(request, 'main/document.html', {'title': 'Восстановление документов'})

def ip(request):
    return render(request, 'main/ip.html', {'title': 'Регистрация ИП'})

def ooo(request):
    return render(request, 'main/ooo.html', {'title': 'Регистрация ООО'})

def spec(request):
    return render(request, 'main/spec.html', {'title': 'Специальные предложения'})

def contact(request):
    return render(request, 'main/contact.html', {'title': 'Контакты'})