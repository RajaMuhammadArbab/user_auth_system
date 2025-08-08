from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','password','password2','role')
        read_only_fields = ('id',)

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate(self, data):
        if data['password'] != data.pop('password2'):
            raise serializers.ValidationError({"password": "Passwords do not match."})
        
        validate_password(data['password'])
        return data

    def create(self, validated_data):
        role = validated_data.pop('role', User.ROLE_USER)
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.role = role
        user.set_password(password)
        
        if not user.username:
            user.username = user.email.split('@')[0]
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','role','is_staff','is_superuser')
        read_only_fields = ('id','email','role','is_staff','is_superuser')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','role')
        read_only_fields = ('id','email','role')
