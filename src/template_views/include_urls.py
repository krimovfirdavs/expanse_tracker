from django.urls import path, include

urlpatterns = [
    path("", include("src.template_views.urls.home")),
    path("", include("src.template_views.urls.users")),
    path("income/", include("src.template_views.urls.income")),
    path("expanse/", include("src.template_views.urls.expanse")),
    path("category/", include("src.template_views.urls.category")),
]
