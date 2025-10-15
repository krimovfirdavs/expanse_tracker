from rest_framework.routers import DefaultRouter

import src.api.views as views

category = DefaultRouter()
category.register("category", views.CategoryModelViewSet)

urlpatterns = category.urls
