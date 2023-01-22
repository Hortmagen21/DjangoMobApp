from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from my_project import settings
from . import forms
from .services import create_new_user


class LogOut(LoginRequiredMixin, LogoutView):
    login_url = '/my_auth/sign_in'


class SignIn(LoginView):
    form_class = forms.SignInForm
    template_name = "signin.html"

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super().form_valid(form)


class SignUp(View):

    def get(self, request):
        form = forms.SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            new_user = create_new_user(form)
            if not new_user:
                messages.info(request, 'User with such name already exist')
                return render(request, 'signup.html', {'form': form})
            login(request, new_user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        return render(request, 'signup.html', {'form': form})



