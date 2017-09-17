from __future__ import unicode_literals

from django.db import models
<<<<<<< HEAD
=======
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email_verified = models.BooleanField(default=False)
>>>>>>> 46348a888dc5f8b0897d407893dd04a699407780
