# yourapp/urls.py
from django.urls import path
from .views import UserProfileCreateView,UserProfileLoginView,UserProfileWelcomeView

urlpatterns = [
    path('signup/', UserProfileCreateView.as_view(), name='signup'),
    path('login/', UserProfileLoginView.as_view(), name='login'),
    path('dashboard/', UserProfileWelcomeView.as_view(), name='dashboard'),
    # Added other URLs for login, dashboard, etc.
]
