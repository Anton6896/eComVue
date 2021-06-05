from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from ecomCore.utils_root.image_name_creator import customer_image_name


class Profile(models.Model):
    """
    for ech user, create unique profile with additional info
    triggers at user create
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio yet")
    avatar = models.ImageField(default='default.jpg', upload_to=customer_image_name)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{str(self.user)}'s - profile "

    class Meta:
        db_table = 'profiles'


# trigger for user creation
def user_creation_receiver(sender, instance, created, *args, **kwargs):
    # create Profile for ech user (Singleton)
    if created:
        return Profile.objects.create(user=instance)


post_save.connect(user_creation_receiver, sender=User)