from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import SignUp

urlpatterns = [
    path('', include('rest_framework.urls')),
    path('user_create', SignUp.as_view(), name="create_user"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
