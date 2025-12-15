from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_mistri/', views.add_mistri, name="add_mistri"),
    path('all_mistri/', views.all_mistri, name="all_mistri"),
]