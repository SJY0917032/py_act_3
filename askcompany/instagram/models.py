from typing import AbstractSet
from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE

class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    message = models.TextField()
