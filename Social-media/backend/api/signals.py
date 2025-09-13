from django.db.models.signals import post_save
from django.dispatch import receiver

from .manager import User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = User(email=instance.email)
        user_profile.save()
        user_profile.follows.set([instance.id])
        print('works', instance)
    if created == False:
        print('something is wrong')