from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.views import View

from my_project import settings
from . import forms
from .models import Profile
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginRequiredMixin, View):
    login_url = '/home/sign_up'

    def get(self, request):
        return render(request, 'index.html')


class LogOut(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)


class SignIn(View):
    def get(self, request):
        form = forms.SignInForm()
        return render(request, 'signin.html', {'form': form})

    def post(self, request):
        form = forms.SignInForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(settings.HOME_URL)
            else:
                messages.info(request, 'Wrong username or password')
                return render(request, 'signin.html', {'form': form})
        return render(request, 'signin.html', {'form': form})


class SignUp(View):

    def get(self, request):
        form = forms.SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User with such name already exist')
                return render(request, 'signup.html', {'form': form})

            else:
                with transaction.atomic():
                    new_user = form.save()
                    login(request, new_user)
                    new_profile = Profile.objects.create(user=new_user, id_user=new_user.id)
                    new_profile.save()
            return HttpResponseRedirect(settings.HOME_URL)
        return render(request, 'signup.html', {'form': form})

