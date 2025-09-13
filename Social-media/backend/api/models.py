from django.db import models
from .manager import User

import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

today = datetime.date.today()

def media_directory_path(instance, filename):
    return 'posts/media/{2}/{0}/{1}'.format(instance.user.user.username,
                                            filename, today)
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,
                                related_name='user_post',
                                on_delete=models.CASCADE)
    media = models.FileField(upload_to=media_directory_path,
                             null=True,
                             blank=True)
    message = models.CharField(null=True, max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User)

class Comment(models.Model):
    user = models.ForeignKey(User,
                                related_name='user_comment',
                                on_delete=models.CASCADE)
    edited = models.BooleanField(blank=True, null=True, default=False)
    post = models.ForeignKey(Post,
                             related_name='post_comment',
                             on_delete=models.CASCADE)
    message = models.CharField(null=True, max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.user.username} \n {self.date}'

class Reply(models.Model):
    user = models.ForeignKey(User,
                                related_name='user_reply',
                                on_delete=models.CASCADE)
    message = models.CharField(null=True, max_length=255)
    date = models.DateTimeField(auto_now_add=True)