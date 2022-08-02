from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('webdev/', views.webdev, name="webdev"),
    path('frontend/', views.frontend, name="frontend"),
    path('backend/', views.backend, name="backend"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
]