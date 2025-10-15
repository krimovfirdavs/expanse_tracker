from rest_framework.viewsets import ModelViewSet

import src.core.models as models
import src.api.serializers as serializer


class CategoryModelViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializer.CategorySerializer
