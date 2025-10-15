from django.urls import path

import src.template_views.views.income as views

urlpatterns = [
    path("list", views.IncomeListView.as_view()),
    path("create", views.IncomeCreateView.as_view()),
    path("update/<int:pk>", views.IncomeUpdateView.as_view()),
    path("delete/<int:pk>", views.IncomeDeleteView.as_view()),
]
