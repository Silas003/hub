from rest_framework import serializers,exceptions,status
from .models import User
from utils import exceptions as exp
from django.db import transaction
from django.contrib.auth.hashers import make_password


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username=serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['id','email', 'username','password',]
        
        read_only_fields=(
            'id',
        )

    def validate_email(self, email):
        if email:
            try:
                if not email.endswith("@st.knust.edu.gh"):
                    raise serializers.ValidationError("Email must be a valid KNUST email address.")
                user = User.objects.get(email=email)
                if user:
                     raise serializers.ValidationError("An account with this email already exists.")
            except User.DoesNotExist:
                pass
        return email

    def validate_password(self,password):
        if password:
            try:
                if len(password) < 8:
                    raise serializers.ValidationError("Password must be at least 8 characters long.")
                
                if password == self.username:
                    raise serializers.ValidationError("Password must not be the same as username.")
            except Exception as e:
                pass 
        return password
     
    def validate_username(self,username):
        if username:
            try:
                user=User.objects.get(username=username)
                if user:
                    raise serializers.ValidationError("Account with this username already exists")
            except User.DoesNotExist:
                pass
        return username
    
    def create(self, validated_data):
        # Hash the password using Django's make_password function
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    @transaction.atomic()
    def save(self, **validated_data):
        return super().save(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True)
    password=serializers.CharField(max_length=255,write_only=True,required=True)
    
    
    class Meta:
        model=User
        fields=['email','password']
        
    def validate_email(self, email):
        if email:
            try:
                if not email.endswith("@st.knust.edu.gh"):
                    raise serializers.ValidationError("Email must be a valid KNUST email address.")
                user = User.objects.get(email=email)
                if not user:
                     raise serializers.ValidationError("Invalid email address")
            except User.DoesNotExist:
                pass
        return email
                