from rest_framework.viewsets import ModelViewSet

import src.core.models as models
import src.api.serializers as serializer


class BaseModelViewSet(ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        qs = qs.filter(added_by=user)
        return qs

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(added_by=user)
