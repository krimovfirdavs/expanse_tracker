from src.bases.base_viewset import *


class CategoryModelViewSet(BaseModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializer.CategorySerializer
