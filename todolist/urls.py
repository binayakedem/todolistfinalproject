from django.contrib import admin
from django.urls import path
from .import views 
urlpatterns = [
    path('',views.home),
    path('create',views.create),
    
    path('delete/<pk>',views.delete),
    path('mark/<pk>',views.mark),
    path('unmark/<pk>',views.unmark),
    path('edit/<pk>',views.edit),
    path('update/<pk>',views.update),

]
