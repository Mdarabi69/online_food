from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import CustomUser, UserProfile


@receiver(post_save, sender=CustomUser)
def post_save_custom_user(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            UserProfile.objects.get(user=instance)
        except:
            UserProfile.objects.create(user=instance)