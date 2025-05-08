from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import SignUpView, profilo_utente, logout_view

app_name ="libreria"
urlpatterns = [
    path("", views.homelib, name="homelib"),
    path("home/", views.homelib, name="homelib2"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path("logout/", logout_view, name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profilo/", profilo_utente, name='profilo'),
    path('profilo/modifica/', views.modifica_profilo, name='modifica_profilo'),
    path('shop/', views.shop, name='shop'),
    path("acquista/<int:oggetto_acquistato_id>", views.acquista_libro, name='acquista'),
    path("autore/<int:autore_id>", views.autori, name="autori"),
    path("libro/<int:libro_id>", views.infolibri, name="infolibri"),
    path("acquisto_completato", views.acquisto_completato, name="acquisto_completato"),
]
