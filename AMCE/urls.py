from django.contrib import admin
from django.urls import include, path

# Views
from AMCE import views

app_name = "AMCE"
urlpatterns = [

path('MG1/', views.MG1, name = "MG1"),
path('', views.index, name = 'index'),
path('registro/', views.registro, name = 'registro'),
path('feed/', views.feed, name = 'feed'),
path('post/', views.post, name = 'post'),
path('profile/', views.profile, name = 'profile'),
path('profile/<str:username>', views.profile, name = 'profile'),

]

