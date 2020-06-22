from django.urls import path
from . import views

urlpatterns = [
    path("<int:problem_id>/", views.index, name="index"),
    path("compile/", views.run_code, name="run_code")
]