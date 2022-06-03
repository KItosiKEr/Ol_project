from distutils.command.upload import upload
from django import views
from django.db import models

class Video(models.Model):
    video = models.ImageField(upload_to='YouTube.IM/%Y/%m')
    title = models.TextField()
    author = models.CharField(max_length=50)
    views = models.IntegerField(default=0, )
    pub_date = models.DateTimeField(auto_now_add=True)


#комментарии,автор,фильтрация,поисковик


# Create your models here.
