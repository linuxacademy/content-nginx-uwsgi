from django.urls import path

from . import views

urlpatterns = [
    path('new', views.UserCreate.as_view(), name='signup'),
]
