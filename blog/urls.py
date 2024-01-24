
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mon_blog, name='mon_blog'),
]