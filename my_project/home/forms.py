from django import forms
from django.forms import CharField, FileField, ModelForm
import my_auth.models as auth_models


class ProfileForm(ModelForm):

    class Meta:
        model = auth_models.Profile
        fields = ['profile_img', 'bio', 'location']

