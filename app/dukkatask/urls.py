# yourapp/urls.py
from django.urls import path
from .views import UserProfileCreateView

urlpatterns = [
    path('signup/', UserProfileCreateView.as_view(), name='signup'),
    # Add other URLs for login, dashboard, etc.
]
