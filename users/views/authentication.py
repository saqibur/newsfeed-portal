from typing import (
    Any,
    Union,
)

from django.forms import Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy



class LoginView(LoginView):
    redirect_authenticated_user: bool = True
    template_name: str = 'users/login.html'



class LogoutView(LogoutView):
    template_name: str ='users/logout.html'



class UserCreateView(CreateView):
    template_name: str  = 'users/register.html'
    form_class: Form = UserCreationForm

    success_url = reverse_lazy('user:login')


    def get(
        self,
        request:  HttpRequest,
        *args:    Any,
        **kwargs: Any,
    ) -> Union[HttpResponseRedirect, HttpResponse]:
        if request.user.is_authenticated:
            return HttpResponseRedirect(redirect_to=reverse_lazy('users:home'))
        else:
            return super().get(self, request, *args, **kwargs)
