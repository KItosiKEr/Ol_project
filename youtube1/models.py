from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Video(models.Model):
    video = models.ImageField(upload_to='YouTube.IM/%Y/%m')
    title = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='videos', null=True)
    views = models.IntegerField(default=0, )
    pub_date = models.DateTimeField(auto_now_add=True)




class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comments', null=True)
    descriptions = models.CharField(max_length=250)
    pub_date = models.DateField(auto_now_add=True)
    




#комментарии,автор,фильтрация,поисковик


# Create your models here.