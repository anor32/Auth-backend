from http.client import responses
from tokenize import TokenError

from django.contrib.auth import authenticate
from django.core.serializers import serialize
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
from users.models import User
from users.serializers import UserRegisterSerializer, UserLoginSerializer, UserProfileSerializer, UserDeleteSerializer, \
    LogoutSerializer


class RegisterUserApi(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()


        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        user_data = {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }

        return Response({
            'user': user_data,
            'access': access_token,
            'refresh': refresh_token
        }, status=status.HTTP_201_CREATED)



class UserLoginApi(APIView):
    serializer_class = UserLoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(username=email,password=password)
        if user:
            if user.is_active:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)

                return Response({
                    'message': 'Вход успешный',
                    'access': access_token,
                    'refresh': refresh_token
                }, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Пользователь некативен"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"error": "Email или пароль указаны неверно"}, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileApi(APIView):
    serializer_class = UserProfileSerializer

    def get(self, request, pk=None):
        if request.user.role == "USER":
            user = request.user
        elif request.user.role in ["ADMIN", "MODERATOR"]:
            if pk is None:
                user = request.user
            else:
                user = get_object_or_404(User, pk=pk)
        else:
            return Response({'error': 'не зарегистрирован'}, status=status.HTTP_403_FORBIDDEN)

        serialized_user = self.serializer_class(user)
        return Response(serialized_user.data, status=status.HTTP_200_OK)

    def patch(self,request,pk):
        if request.user.role == "USER":
            user = request.user
        elif request.user.role in ["ADMIN",]:
            if pk is None:
                user = request.user
            else:
                user = get_object_or_404(User, pk=pk)
        else:
            return Response({'error': 'не зарегистрирован'}, status=status.HTTP_403_FORBIDDEN)
        serializer =self.serializer_class(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk):
        if request.user.role == "USER":
            user = request.user
        elif request.user.role in ["ADMIN", ]:
            if pk is None:
                user = request.user
            else:
                user = get_object_or_404(User, pk=pk)
        else:
            return Response({'error': 'не зарегистрирован'}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.serializer_class(user, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    serializer_class = LogoutSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        refresh_token = serializer.validated_data['refresh_token']
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Успешный выход'}, status=status.HTTP_200_OK)
        except TokenError :
            return Response({'error': 'Невалидный токен или истек срок пользования '}, status=status.HTTP_400_BAD_REQUEST)

class DeleteUser(APIView):
    serializer_class = UserDeleteSerializer
    def delete(self,request,pk):
        if request.user.role == "USER":
            user = request.user
        elif request.user.role in ["ADMIN", ]:
            if pk is None:
                user = request.user
            else:
                user = get_object_or_404(User, pk=pk)
        else:
            return Response({'error': 'не зарегистрирован или нет прав'}, status=status.HTTP_403_FORBIDDEN)
        password = request.data.get('password')

        if not password or not request.user.check_password(password):
            return Response({'error': 'Неверный пароль'}, status=status.HTTP_400_BAD_REQUEST)
        user.is_active = False
        user.save()

        refresh_token = request.data.get('refresh_token')
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
            except Exception:
                return Response({'message':'Токен уже удален'},status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Аккаунт Успешно удален'},status=status.HTTP_200_OK)
class AdminManageRoles(APIView):
    def post(self):
        pass
        #if role == admin:
        #{user:id role:'moderator',status,''}

        # должен назначать разрешения роли что она может с книгами делать а что не может также назначачть пользователям роли