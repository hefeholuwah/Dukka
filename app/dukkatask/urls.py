# yourapp/urls.py
from django.urls import path
from .views import UserProfileCreateView,UserProfileLoginView

urlpatterns = [
    path('signup/', UserProfileCreateView.as_view(), name='signup'),
    path('login/', UserProfileLoginView.as_view(), name='login'),
    # Add other URLs for login, dashboard, etc.
]
