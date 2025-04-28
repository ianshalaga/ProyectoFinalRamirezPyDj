from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "user"

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("signup/", views.CustomSignupView.as_view(), name="signup"),
    path("detail/", views.UserDetailView.as_view(), name="user_detail"),
    path("update/", views.UserUpdateView.as_view(), name="user_update"),
    path('password_change/', views.CustomPasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='user/password_change_done.html'
    ), name='password_change_done'),
]
