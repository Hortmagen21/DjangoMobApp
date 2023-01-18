from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, EmailField
from .forms_style import AuthenticationStyle


class SignInForm(AuthenticationForm, AuthenticationStyle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"] = CharField(widget=forms.TextInput(attrs=self.get_attrs()))
        self.fields["password"] = CharField(min_length=6, widget=forms.PasswordInput(attrs=self.get_attrs()))


class SignUpForm(UserCreationForm, AuthenticationStyle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"] = CharField(widget=forms.TextInput(attrs=self.get_attrs()))
        self.fields["email"] = EmailField(max_length=100, widget=forms.EmailInput(attrs=self.get_attrs()))
        self.fields["password1"] = CharField(min_length=6, widget=forms.PasswordInput(attrs=self.get_attrs()))
        self.fields["password1"].label = "Password"
        self.fields["password2"] = CharField(min_length=6, widget=forms.PasswordInput(attrs=self.get_attrs()))
        self.fields["password2"].label = "Password Confirm"

