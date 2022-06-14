from msilib.schema import ListView
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from youtube1.models import Video
from youtube1.serializers import VideoSerializers,AuthorSerializers
from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()

class VideoView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # filter_backends = (DjangoFilterBackend)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


    def retrieve(self, request, *arg, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = VideoSerializers(instance)
        return Response(serializer.data)


class AuthorView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AuthorSerializers 


# class VideoCreateView(CreateAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializers

# class VideoUpdateDelete(RetrieveUpdateDestroyAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializers
#     # Create your views here.
