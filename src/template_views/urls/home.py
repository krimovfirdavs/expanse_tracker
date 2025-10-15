from django.urls import path

import src.template_views.views.home as views

urlpatterns = [
    path("home", views.HomeView.as_view())
]
