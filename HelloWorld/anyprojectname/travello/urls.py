from django.urls import path
from . import views

urlpatterns = [
    path('', views.travello, name='travello_home'),
]