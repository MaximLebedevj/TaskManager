import datetime

import jwt
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import get_object_or_404, render
from rest_framework import permissions, status, viewsets
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializer import (CreateOrganizationSerialize, UpdateProfileSerialize,
                         UserLoginSerialize, UserLogoutSerialize,
                         UserRegisterSerialize, UserSerializeProfile)


class RegisterApiView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerialize


class LoginApiView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerialize

    def create(self, request, *args, **kwargs):
        try:
            user_login = request.data['username']
        except KeyError:
            return Response({"errors": {"detail": "Please, enter login"}},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            password = request.data['password']
        except KeyError:
            return Response({"errors": {"detail": "Please, enter password"}},
                            status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=user_login, password=password)
        if user is None:
            return Response({"errors": "Invalid data"},
                            status=status.HTTP_400_BAD_REQUEST)
        login(request, user)

        user = request.user
        print("--------")
        print(user)

        return Response({"success": "The user has been logged in"},
                        status=status.HTTP_200_OK)


class UserApiView(APIView):
    def get(self, request):
        user = User.objects.filter(id=request.user.id).first()
        serializer = UserSerializeProfile(user)

        return Response(serializer.data)


class LogoutApiView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': "Logout successful"})


class UpdateProfile(UpdateAPIView):

    serializer_class = UpdateProfileSerialize
    queryset = get_user_model().objects.all()

    def get(self, request):
        global user_id
        user_id = request.user.id
        return Response(user_id, status=status.HTTP_200_OK)

    def get_object(self):
        return User.objects.get(pk=user_id)


class CreateOrganization(CreateAPIView):
    serializer_class = CreateOrganizationSerialize
