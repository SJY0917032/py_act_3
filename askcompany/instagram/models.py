from typing import AbstractSet
from django.db import models

class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class Post(BaseModel):
    message = models.TextField()
