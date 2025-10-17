from rest_framework import serializers

import src.core.models as models
from django.contrib.auth.models import User


class UserRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class CategoryRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("id", "name")
