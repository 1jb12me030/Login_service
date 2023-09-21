# login_service/urls.py
from django.urls import path
from .views import UserRegistration, UserLogin, ReferralCode

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user-registration'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('referral/', ReferralCode.as_view(), name='generate-referral-code'),
]
