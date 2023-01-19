from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('settings', views.Settings.as_view(), name='settings')
]



