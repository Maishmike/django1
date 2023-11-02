from django.urls import path
from . import views

app_name = 'teachers'
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('add/', views.add, name='add'),
    path('viewdata/', views.view, name='viewdata'),
    path('delete/<id>', views.delete, name='delete'),
    path('insert', views.insert, name='insert'),
    path('edit/<id>', views.edit, name='edit'),
    path('sliders/', views.sliders, name='sliders')

]
