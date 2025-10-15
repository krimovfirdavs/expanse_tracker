from django.urls import path

import src.template_views.views.expanse as views

urlpatterns = [
    path("list", views.ExpanseListView.as_view()),
    path("create", views.ExpanseCreateView.as_view()),
    path("update/<int:pk>", views.ExpanseUpdateView.as_view()),
    path("delete/<int:pk>", views.ExpanseDeleteView.as_view()),
]
