from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class Home(LoginRequiredMixin, View):
    login_url = '/my_auth/sign_in'

    def get(self, request):
        return render(request, 'index.html')


