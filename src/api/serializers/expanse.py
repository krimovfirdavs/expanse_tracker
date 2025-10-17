from src.bases.serializers.base_serializer import *


class ExpanseSerializer(BaseSerializer):
    class Meta:
        model = models.Expanse
        exclude = ("added_by",)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["category"] = CategoryRelationSerializer(instance.category).data
        return data
