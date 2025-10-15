from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name="%(class)s_added_by")

    class Meta:
        abstract = True
