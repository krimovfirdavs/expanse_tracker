from django.urls import path, include

urlpatterns = [
    path("", include("src.template_views.include_urls"))
]
