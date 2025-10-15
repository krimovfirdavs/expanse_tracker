from django.urls import path

import src.template_views.views.users as views

urlpatterns = [
    path("", views.LoginUserView.as_view(), name="login"),
    path("logout", views.LogoutUserView.as_view(), name="logout"),
    path("register", views.RegisterUserView.as_view(), name="register"),
]
