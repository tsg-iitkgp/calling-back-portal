from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class CustomUser(AbstractUser):
#     # [(value, human readable name),....] to create a radio selection field
#     roles = [('hod','Department Head'), ('warden','Hall Warden')]
#     role = models.CharField(max_length=20, default='hod', choices = roles, blank=False, null=False)
#     is_active = models.BooleanField(default=False)
#     department = models.CharField(max_length=500, blank=True)
#     hall = models.CharField(max_length=500, blank=True)

#     def __str__(self):
#         return self.username
