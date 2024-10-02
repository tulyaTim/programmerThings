from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Skill

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """Override the default create method to handle password hashing."""
        user = User(
            username=validated_data['username'], 
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'date_of_birth', 'profile_pic', 'cover_pic']
        extra_kwargs = {
            'user': {'read_only': True} 
        }

    def create(self, validated_data):
        profile = Profile.objects.create(
            user=validated_data['user'],
            date_of_birth=validated_data.get('date_of_birth'),
            profile_pic=validated_data.get('profile_pic'),
            cover_pic=validated_data.get('cover_pic')
        )
        return profile
    

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'user', 'name', 'proficiency_level']
        read_only_fields = ['user']


