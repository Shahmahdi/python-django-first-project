from django.urls import path
from . import views

urlpatterns = [
  path('function', views.hello_world),
  path('class', views.HelloMahdi.as_view()),
]