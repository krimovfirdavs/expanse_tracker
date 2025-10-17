from src.bases.base_viewset import *


class ExpanseModelViewSet(BaseModelViewSet):
    queryset = models.Expanse.objects.all()
    serializer_class = serializer.ExpanseSerializer
