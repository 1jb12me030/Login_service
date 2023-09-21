from django.shortcuts import render

# Create your views here.
# login_service/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db import IntegrityError
from django.contrib.auth.models import User as AuthUser
from .models import Referral, UserProfile
from .serializers import *

class UserRegistration(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        user = AuthUser.objects.filter(username=username).first()

        if user is None or not user.check_password(password):
            return Response({'detail': 'Invalid credentials'}, status=400)

        return Response({'detail': 'Login successful'})

import random
import string

class ReferralCode(APIView):
    def get(self, request):
        referral_code = self.generate_referral_code()
        return Response({'referral_code': referral_code})

    def generate_referral_code(self):
        # Define characters to use for generating the code
        characters = string.ascii_letters + string.digits  # Alphanumeric characters

        while True:
            # Generate a random code of length 6
            code = ''.join(random.choice(characters) for _ in range(6))

            # Check if the code is already in use
            if not UserProfile.objects.filter(referral_code=code).exists():
                return code

