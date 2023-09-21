# login_service/serializers.py
from rest_framework import serializers
from .models import Referral, UserProfile

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Referral
import random
import string
class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        # Generate a referral code
        referral_code = self.generate_referral_code()

        # Create the user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Create a user profile with the referral code
        UserProfile.objects.create(user=user, referral_code=referral_code)

        return user

    def generate_referral_code(self, length=6):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))