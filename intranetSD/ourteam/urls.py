from django.urls import path
from . import views

urlpatterns = [
    path('', views.ourteam, name='ourteam'),
    path('teachers', views.ourteachers, name='teachers')
]