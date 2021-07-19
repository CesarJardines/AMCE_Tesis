from django.contrib import admin
from django.urls import include, path

# Views
from AMCE import views

app_name = "AMCE"
urlpatterns = [

path('MG1/', views.MG1, name = "MG1"),
path('', views.index, name = 'index'),
path('registro/', views.registro, name = 'registro'),

]

