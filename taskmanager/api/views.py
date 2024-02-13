import datetime

import jwt
from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import get_object_or_404, render
from rest_framework import permissions, status, viewsets
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializer import (UserLoginSerialize, UserLogoutSerialize,
                         UserSerialize, UserSerializeProfile)


class RegisterApiView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerialize


class LoginApiView(CreateAPIView):
    serializer_class = UserLoginSerialize

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if User is None:
            raise AuthenticationFailed('No such user')
        if not user.check_password(password):
            raise AuthenticationFailed('Invalid password')

        payload = {
            "id": user.id,
            "email": user.email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt token': token
        }

        return response


class UserApiView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed("User is unauthenticated")

        try:
            payload = jwt.decode(token, 'secret', algorithms='HS256')

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("User is unauthenticated")

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializeProfile(user)

        return Response(serializer.data)


class LogoutApiView(CreateAPIView):
    serializer_class = UserLogoutSerialize

    def get(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'successful logout'
        }

        return response
