from django.urls import path

from users.views.authentication import (
    UserCreateView,
    LoginView,
    LogoutView,
)
from users.views.homepage import HomeView
from users.views.settings import SettingsView

app_name: str = 'users'

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('home/', HomeView.as_view(), name='home'),
    path('success/', HomeView.as_view(), name='success'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('settings/', SettingsView.as_view(), name='settings'),
]
