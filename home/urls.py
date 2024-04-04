from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = "inicio") ,
    path('login/', views.login, name = "login") ,
    path('signup/', views.signup, name = "signup"),
    path('personuser/', views.personuser, name = "personuser"),
    path('avaliacaogeral/', views.avaliacaogeral, name = "avaliacaogeral")
]

