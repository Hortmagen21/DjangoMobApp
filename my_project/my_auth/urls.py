from django.urls import path
from . import views

urlpatterns = [
    path('sign_up', views.SignUp.as_view(), name='signup'),
    path('sign_in', views.SignIn.as_view(), name='signin'),
    path('logout', views.LogOut.as_view(), name='logout'),
]