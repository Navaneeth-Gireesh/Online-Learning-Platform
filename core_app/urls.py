from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('base/',views.base, name = 'base'),
    path('error_404/', views.error_404, name = 'error_404'),
]