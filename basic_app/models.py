from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):
    # create relationship (don't inherit from User)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add any additional attributes
    portfolio_site = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        # build-in attribute of django.contrib.auth.models.User
        return self.user.username
