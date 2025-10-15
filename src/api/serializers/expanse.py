from src.bases.serializers.base_serializer import *


class ExpanseSerializer(BaseSerializer):
    class Meta:
        model = models.Expanse
        fields = "__all__"
