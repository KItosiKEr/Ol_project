from dataclasses import field
from rest_framework.serializers import ModelSerializer

from .models import Video

from django.contrib.auth import get_user_model


User = get_user_model()

class VideoSerializers(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

        read_only_fields = ('author', )

class AuthorSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'