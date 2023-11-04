from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, CustomeUser



@receiver(post_save, sender=CustomeUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=Profile)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user = CustomeUser.objects.get(email=instance.user.email)
        user.is_verified = True
        user.save()
    




