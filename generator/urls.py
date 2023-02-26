from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('generated_password/', views.password, name='password'),
    path('about/', views.about, name='about')

]
