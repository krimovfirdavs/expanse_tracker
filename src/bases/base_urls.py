from django.urls import path, include

urlpatterns = [
    path("", include("src.api.include_routers")),
    path("", include("src.bases.integrate_urls")),
    path("", include("src.template_views.include_urls"))
]
