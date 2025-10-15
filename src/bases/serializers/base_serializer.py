from rest_framework import serializers

import src.core.models as models


class BaseSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["added_at"] = instance.added_at.strftime("%Y-%m-%d %H:%M")
        data["updated_at"] = instance.updated_at.strftime("%Y-%m-%d %H:%M")
        return data
