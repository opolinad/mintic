from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('login/', views.login),
    path('home-admin/', views.home_admin),
    path('home-estudiante/', views.home_student),
    path('api/login', views.login_api),
    path('api/projects', views.projects_api),
    path('api/projects/<int:id>', views.projects_api),
    path('api/users', views.users_api),
    path('api/users/<int:id>', views.users_api),
]