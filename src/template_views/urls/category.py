from django.urls import path

import src.template_views.views.category as views

urlpatterns = [
    path("list", views.CategoryListView.as_view()),
    path("create", views.CategoryCreateView.as_view()),
    path("update/<int:pk>", views.CategoryUpdateView.as_view()),
    path("delete/<int:pk>", views.CategoryDeleteView.as_view()),
]
