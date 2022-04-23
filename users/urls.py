"""_summary_
"""
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import account, login, signup

urlpatterns=[
    path("accounts/account", account, name="account"),
    path("accounts/login", login, name="login"),
    path("accounts/signup", signup, name="signup"),
    path("accounts/logout", LogoutView.as_view(), name="logout"),
]
