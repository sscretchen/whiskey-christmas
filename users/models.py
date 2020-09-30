from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from PIL import Image

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models. TextField(max_length=1000, blank=True)
    image = models.ImageField(blank=True, null=True, default='users/no_profile_pic.png', upload_to='users')
    slug = models.SlugField(editable=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        # Display username in admin panel
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)
