from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def hello_world(request):
  return HttpResponse("Hello World")

class HelloMahdi(View):
  def get(self, request):
    return HttpResponse("Hello Mahdi")
