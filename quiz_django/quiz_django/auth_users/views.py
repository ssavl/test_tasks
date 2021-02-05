from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import FormView
from .forms import SignUpForm
# Create your views here.


def start(request):
    return render(request, 'index.html')


class MyLogoutView(LogoutView):
    next_page = '/'


class MyLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm



    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super().form_valid(form)


class RegisterView(FormView):
    success_url = '/'
    form_class = SignUpForm
    template_name = 'signup.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super().form_valid(form)