from django.urls import path
from . import views

app_name = "app2"

urlpatterns = [
    path('', views.home, name='home'),
    path('about2/', views.about, name='about2')
]