from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("info/<str:section>", views.info, name="index"),
    path("login/", views.login_view, name="login"),
    path("accounts/login/", views.login_view, name="login_sys"),
    path("github/authorized/", views.github, name="github"),
    path("logout/", views.logout_view, name="logout"),
    path("purchase/", views.purchase, name="purchase"),
    path("create-payment-intent", views.create_payment, name="create-payment-intent"),
]