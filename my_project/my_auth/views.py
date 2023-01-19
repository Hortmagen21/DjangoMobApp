from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from my_project import settings
from . import forms
from .models import Profile


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
            username = form.cleaned_data.get("username")
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User with such name already exist')
                return render(request, 'signup.html', {'form': form})
            else:
                with transaction.atomic():
                    new_user = form.save()
                    login(request, new_user)
                    new_profile = Profile.objects.create(user=new_user, id_user=new_user.id)
                    new_profile.save()
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        return render(request, 'signup.html', {'form': form})



