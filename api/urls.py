from django.urls import path
from . import views

urlpatterns = [
    path("problems/", views.problems, name="problems_api")
]