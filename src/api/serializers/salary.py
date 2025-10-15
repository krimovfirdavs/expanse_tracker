from src.bases.serializers.base_serializer import *


class SalarySerializer(BaseSerializer):
    class Meta:
        model = models.Income
        fields = "__all__"
