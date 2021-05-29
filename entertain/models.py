import time

from django.db import models

import string
import random
import time
def code_generator():
    length = 8
    while True:
        code = ''.join(random.choices(string.ascii_uppercase,k=length))
        if Room.objects.filter(code = code).count() == 0:
            break
    return code

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=30,unique=True,default='')
    host = models.CharField(max_length=50, unique=True,default='')
    description = models.TextField(blank=True, null=True)
    user_pause = models.BooleanField(default=False, null=False)
    vote_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
