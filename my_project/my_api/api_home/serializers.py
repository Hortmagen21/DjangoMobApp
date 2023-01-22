from rest_framework import serializers
import my_auth.models as auth_models


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = auth_models.Profile
        fields = ['profile_img', 'bio', 'location']
