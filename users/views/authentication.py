from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy



class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'users/login.html'



class LogoutView(LogoutView):
    template_name ='users/logout.html'



class UserCreateView(CreateView):
    template_name = 'users/register.html'
    form_class    = UserCreationForm
    success_url   = reverse_lazy('users:login')


    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(redirect_to=reverse_lazy('users:home'))
        else:
            return super().get(self, request, *args, **kwargs)
