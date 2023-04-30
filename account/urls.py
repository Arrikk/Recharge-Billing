from django.urls import path
from django.urls import path, re_path
from stripe import Account
from .views import SignupView


urlpatterns = [
    path('signup/', SignupView.as_view())
]