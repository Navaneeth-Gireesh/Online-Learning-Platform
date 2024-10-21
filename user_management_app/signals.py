from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import Profile


# Signal to Create profile when user Registers
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Signal to Save the profile when a profile is created
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()