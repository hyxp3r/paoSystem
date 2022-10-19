from tabnanny import verbose
from django.db import models

from django.contrib.auth.models import User
 
 
class UserProfile(models.Model):
    user = models.OneToOneField(User,  on_delete = models.CASCADE)
    post = models.CharField(max_length = 200, verbose_name = "Должность" , null = True)
    department = models.CharField(max_length = 30, verbose_name = "Отдел", null = True)

    def __unicode__(self):
        return self.post
