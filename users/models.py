from django.contrib.auth.models import AbstractUser
from django.db import models

from users.manager import UserManager
from users.services import upload_path

NULLABLE = {'null': True, 'blank': True}


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='user_email', max_length=100, unique=True)
    phone = models.CharField(verbose_name='user_phone', max_length=50, **NULLABLE)
    telegram = models.CharField(verbose_name='user_phone', max_length=50, **NULLABLE)
    avatar = models.ImageField(verbose_name='users_avatar', upload_to=upload_path, **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()


