from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProfileList


urlpatterns = [
    path('profile_settings', ProfileList.as_view(), name="profile_settings"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
