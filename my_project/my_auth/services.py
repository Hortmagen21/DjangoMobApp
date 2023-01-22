from django.contrib.auth.models import User
from django.db import transaction
from .models import Profile


def create_new_user(form):
    username = form.cleaned_data.get("username")
    if User.objects.filter(username=username).exists():
        return None
    else:
        with transaction.atomic():
            new_user = form.save()
            new_profile = Profile.objects.create(user=new_user, id_user=new_user.id)
            new_profile.save()
