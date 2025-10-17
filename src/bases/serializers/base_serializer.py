from src.bases.serializers.relation_serializer import *


class BaseSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["added_at"] = instance.added_at.strftime("%Y-%m-%d %H:%M")
        data["updated_at"] = instance.updated_at.strftime("%Y-%m-%d %H:%M")
        data["added_by"] = UserRelationSerializer(instance.added_by).data
        return data
