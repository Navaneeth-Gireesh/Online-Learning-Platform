from django.urls import path
from . import views

urlpatterns = [
    path('Expert_Advice', views.expert_advice, name = 'expert_advice')
]