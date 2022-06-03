from xml.etree.ElementInclude import include
from django.urls import path

from .views import VideoView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/v1/video', VideoView)


urlpatterns = router.urls
# [
#     path('api/v1/', include(router.urls))  
#     path('api/v1/Video/create',VideoCreateView.as_view()),
#     path('api/v1/Video/<int:pk>', VideoUpdateDelete.as_view()),
# ]
