from django.urls import path, include
from django.contrib.auth.models import User
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('rooms/',views.getRooms,name='rooms'),
    path('rooms/<str:pk>/',views.getRoom),
]