from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, EmailField, BooleanField


class SignInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"] = CharField(widget=forms.TextInput(attrs=self.get_char_field_attrs()))
        self.fields["password"] = CharField(min_length=6,
                                            widget=forms.PasswordInput(attrs=self.get_char_field_attrs()))
        self.fields["remember_me"] = BooleanField(required=False, widget=forms.CheckboxInput(attrs={"style": "outline: none;"}))

    @staticmethod
    def get_char_field_attrs():
        return {"class": "bg-gray-200 mb-2 shadow-none dark:bg-gray-800"}


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"] = CharField(widget=forms.TextInput(attrs=self.get_char_field_attrs()))
        self.fields["email"] = EmailField(max_length=100,
                                          widget=forms.EmailInput(attrs=self.get_char_field_attrs()))
        self.fields["password1"] = CharField(min_length=6,
                                             widget=forms.PasswordInput(attrs=self.get_char_field_attrs()))
        self.fields["password1"].label = "Password"
        self.fields["password2"] = CharField(min_length=6,
                                             widget=forms.PasswordInput(attrs=self.get_char_field_attrs()))
        self.fields["password2"].label = "Password Confirm"

    @staticmethod
    def get_char_field_attrs():
        return {"class": "bg-gray-200 mb-2 shadow-none dark:bg-gray-800"}

