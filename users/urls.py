from django.urls import path

from users.views.authentication import (
    UserCreateView,
    LoginView,
    LogoutView,
)
from users.views.homepage import (
    HomeView,
    NewsfeedView,
)
from users.views.settings import SettingsView
from users.views.password_reset import (
    CustomPasswordResetCompleteView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetDoneView,
    CustomPasswordResetView,
)

app_name: str = "users"

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register"),
    path("home/", HomeView.as_view(), name="home"),
    path("success/", HomeView.as_view(), name="success"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("settings/", SettingsView.as_view(), name="settings"),
    path("newsfeed/", NewsfeedView.as_view(), name="newsfeed"),
    path("password_reset/", CustomPasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/complete/",
        CustomPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
