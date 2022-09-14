"""mlproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

def test(request):
  return HttpResponse('テストページ')


def test(request):
  return HttpResponse('テストページ')

def test2(request):
  # test2html = loader.render_to_string('test2.html')
  test2html = render(request,'test2.html')
  return test2html

urlpatterns = [
    # テスト用
    path('test/', test),
    path('test2/', test2),
]