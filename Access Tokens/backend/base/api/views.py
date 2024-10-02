from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from .models import Profile, Skill
from .serializers import UserSerializer, ProfileSerializer, SkillSerializer
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def signup(request):
    serialiser = UserSerializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        # token = Token.objects.create(user=user)
        return Response({"user":serialiser.data})
    return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def login(request):
#     user = get_object_or_404(User, username=request.data['username'])
#     if not user.check_password(request.data['password']):
#         return Response({"detail":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
#     token, created = Token.objects.get_or_create(user=user)
#     serialiser = UserSerializer(instance=user)
#     return Response({"token":token.key, "user":serialiser.data})


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['password'] = user.password
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_skills(request):
    if request.method == 'GET':
        skills = Skill.objects.filter(user=request.user)
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data
        serializer = SkillSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Automatically associate the user with the skill
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
    ]
    
    return Response(routes)