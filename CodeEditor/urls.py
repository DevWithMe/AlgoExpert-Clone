from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("compile/", views.run_code, name="run_code")
]