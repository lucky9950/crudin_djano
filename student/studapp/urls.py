from django.contrib import admin
from django.urls import path
from studapp import views

urlpatterns = [
   
    path('base', views.base),
    path('create/',views.create),
    path('dashboard',views.dashboard),
    path('delete/<int:id>',views.delete),
    path('update/<int:id>',views.update)
]
