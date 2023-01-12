from django.db import models


class Profile(models.Model):
    pass
    # user = pass
    # id_user = pass
    # bio =
    profile_img = models.ImageField(upload_to='profile_images', default='blank_profile_img.png')
    # location =
