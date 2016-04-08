from django.contrib.auth.models import User
from django.db import models
from django.dispatch.dispatcher import receiver


class UserInfo(models.Model):
    """Model for storing extra information related to a user.
    """

    owner = models.OneToOneField(User, related_name='extra_info',
            primary_key=True, help_text="User associated with this instance")

    email = models.EmailField(unique=True, null=False,
            help_text="email to identify the organization")

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'


@receiver(models.signals.post_save, sender=User)
def create_extra_info(sender, instance, created, **kwargs):
    """ Creates the UserInfo instance for each new user upon creation"""
    if created :
        UserInfo.objects.create(owner=instance)


