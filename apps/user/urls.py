from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("login", views.CustomLoginView.as_view(), name="login"),
    path("logout", views.CustomLogoutView.as_view(), name="logout"),
    path("signup", views.CustomSignupView.as_view(), name="signup"),
]
