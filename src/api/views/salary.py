from src.bases.base_viewset import *


class IncomeModelViewSet(BaseModelViewSet):
    queryset = models.Income.objects.all()
    serializer_class = serializer.SalarySerializer
