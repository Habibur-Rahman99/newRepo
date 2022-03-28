from django.db import models
from django.contrib.auth.models import User
from numpy import blackman
# Create your models here.

class UserPortfolioInfo(models.Model):

    user  = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to = 'media/profile_pics',blank = True)

    def __str__(self):
        return self.user.username

