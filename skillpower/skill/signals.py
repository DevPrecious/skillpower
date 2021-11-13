from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Community, Office, Profile, School

# profile
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# school
@receiver(post_save, sender=User)
def create_school_profile(sender, instance, created, **kwargs):
    if created:
        School.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_school_profile(sender, instance, **kwargs):
    instance.school.save()

# office
@receiver(post_save, sender=User)
def create_office_profile(sender, instance, created, **kwargs):
    if created:
        Office.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_office_profile(sender, instance, **kwargs):
    instance.office.save()

#community
@receiver(post_save, sender=User)
def create_community_profile(sender, instance, created, **kwargs):
    if created:
        Community.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_community_profile(sender, instance, **kwargs):
    instance.community.save()