from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import SignUp

urlpatterns = [
    path('user_create', SignUp.as_view(), name="create_user"),
    path('', include('rest_framework.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
