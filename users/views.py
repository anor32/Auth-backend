from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from users.models import User
from users.serializers import UserRegisterSerializer, UserLoginSerializer


class RegisterUserApiView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "Пользователь успешно зарегистрирован",
                "user_id": user.id,
                # можно вернуть другие данные, например токен
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLogin(APIView):
    serializer_class = UserLoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(username=email,password=password)
        if user:
            if user.is_active:
                return Response({"message":"Вход успешный"},status=status.HTTP_200_OK)
            else:
                return Response({"message": "Пользователь некативен"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"error": "Email или пароль указаны неверно"}, status=status.HTTP_401_UNAUTHORIZED)


# class UserUpdate()
# class UserLogout()
# class DeleteUser()
