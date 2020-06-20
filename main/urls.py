from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("info/<str:section>", views.info, name="index"),
    path("login/", views.login, name="login"),
    path("github/authorized/", views.github, name="github")
]