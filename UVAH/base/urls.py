from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('roadmap/', views.roadmap, name='roadmap'),
    path('webdev/', views.webdev, name="webdev"),
    path('frontend/', views.frontend, name="frontend"),
    path('backend/', views.backend, name="backend"),
    path('login/', views.user_login, name="login"),
    path('register/', views.user_register, name="register"),
    path('submit/', views.submit, name="submit"),
    path('test/', views.test, name="test")
]