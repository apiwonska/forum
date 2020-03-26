from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from users.models import CustomUser


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(pre_save, sender=CustomUser)
def add_default_picture(sender, instance, **kwargs):
    """
    Add default avatar picture if avatar field is blank.
    """
    user = instance
    if user.avatar == '':
        user.avatar = 'users/blank-profile-picture.svg'
