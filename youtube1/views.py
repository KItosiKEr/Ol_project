from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from youtube1.models import Video
from youtube1.serializers import VideoSerializers

class VideoView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers

    def retrieve(self, request, *arg, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = VideoSerializers(instance)
        return Response(serializer.data)



# class VideoCreateView(CreateAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializers

# class VideoUpdateDelete(RetrieveUpdateDestroyAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializers
#     # Create your views here.
