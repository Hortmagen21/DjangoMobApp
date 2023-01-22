from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .services import get_profile_form, post_profile_form
from my_project import settings
from .forms import ProfileForm
import my_auth.models as auth_models


class Home(LoginRequiredMixin, View):
    login_url = '/my_auth/sign_in'

    def get(self, request):
        return render(request, 'index.html')


class Settings(LoginRequiredMixin, View):

    def get(self, request):
        form = get_profile_form(request=request)

        if form:
            return render(request, 'setting.html', {'form': form})
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    def post(self, request):
        form = post_profile_form(request=request)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/home/settings")
        return HttpResponse(status=400)


