from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('home-admin/', views.home_admin),
    path('home-profesor/', views.home_proffesor),
    path('home-estudiante/', views.home_student),
    path('api/login', views.login_api),
]