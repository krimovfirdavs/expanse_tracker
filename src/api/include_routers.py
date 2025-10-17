from rest_framework.routers import DefaultRouter

import src.api.views as views

router = DefaultRouter()
router.register("income", views.IncomeModelViewSet)
router.register("expanse", views.ExpanseModelViewSet)
router.register("category", views.CategoryModelViewSet)

urlpatterns = router.urls
