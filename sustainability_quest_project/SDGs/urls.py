from django.urls import path
from . import views


urlpatterns = [    
    path('', views.SDGs, name='SDGs'),
    path('SDGs/<int:pk>/', views.goal_detail, name='goal_detail'),
]
