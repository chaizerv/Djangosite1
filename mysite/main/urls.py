from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('egrul/', views.egrul, name='egrul'),
    path('egrn/', views.egrn, name='egrn'),
    path('i_egrul/', views.i_egrul, name='i_egrul'),
    path('document/', views.document, name='document'),
    path('ip/', views.ip, name='ip'),
    path('ooo/', views.ooo, name='ooo'),
    path('spec/', views.spec, name='spec'),
    path('contact/', views.contact, name='contact'),



]