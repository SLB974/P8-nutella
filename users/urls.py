"""_summary_
"""
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import account, signup

urlpatterns=[
    path("accounts/account", account, name="account"),
    path("accounts/signup", signup, name="signup"),
    path("accounts/login", LoginView.as_view(), name="login"),
    path("account/logout", LogoutView.as_view(), name="logout"),
]
