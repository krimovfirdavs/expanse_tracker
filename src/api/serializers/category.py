from src.bases.serializers.base_serializer import *


class CategorySerializer(BaseSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"
