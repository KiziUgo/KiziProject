from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    company_name = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return f'{self.user.username} profile'




