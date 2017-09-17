from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser

# User Model: Extension of Built-In User Model for login/authentication
class User(AbstractUser):
    email_verified = models.BooleanField(default=False)
