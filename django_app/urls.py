from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_f, name="login"),
    path('logout/', views.logout_f, name="logout"),
    path('register/', views.register, name="register"),
    path('main/', views.main, name="main"),
    path('diagram/', views.diagram, name="diagram"),
    path('delete/<str:model_type>/<str:pk>/', views.delete_record, name='delete_record'),
]
