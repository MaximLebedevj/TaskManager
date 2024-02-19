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

from .models import Organization, Project, User
from .serializer import (CreateOrganizationSerialize, CreateProjectSerialize,
                         OrganizationViewSerialize,
                         ShowAllOrganizationsSerialize, UpdateProfileSerialize,
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


class UpdateApiProfile(UpdateAPIView):

    serializer_class = UpdateProfileSerialize
    queryset = get_user_model().objects.all()

    def get(self, request):
        serializer = self.serializer_class(
            UpdateProfileSerialize, many=True, context={'request'})
        global user_id
        user_id = request.user.id
        return Response(status=status.HTTP_200_OK)

    def get_object(self):
        return User.objects.get(pk=user_id)


class CreateApiOrganization(CreateAPIView):
    serializer_class = CreateOrganizationSerialize


class OrganizationApiView(APIView):
    def get(self, request, organization_pk):
        queryset = Organization.objects.filter(id=organization_pk)
        serializer = OrganizationViewSerialize(queryset, many=True)
        return Response(serializer.data)


class ShowAllOrganizationsApi(ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = ShowAllOrganizationsSerialize

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ShowAllOrganizationsSerialize(queryset, many=True)
        return Response(serializer.data)


class CreateProjectApi(CreateAPIView):
    serializer_class = CreateProjectSerialize

    def create(self, request, organization_pk):

        organization = Organization.objects.filter(id=organization_pk).first()

        project = Project(name=request.data['name'],
                          organization_id = organization)

        project.save()
        return Response({"success": "project was created"},
                        status=status.HTTP_200_OK)
