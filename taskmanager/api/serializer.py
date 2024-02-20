import jwt
from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.fields import CurrentUserDefault
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator

from .models import Organization, Project, User


class UserRegisterSerialize(serializers.ModelSerializer):

    password1 = serializers.CharField(
        write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'full_name',
            'password1',
            'password2']

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Пароли не совпадают."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            full_name=validated_data['full_name']
        )

        user.set_password(validated_data['password1'])
        user.save()

        return user


class UserLoginSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserLogoutSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class UserSerializeProfile(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'full_name',
            'email',
            'password',
            'telegram_name']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UpdateProfileSerialize(serializers.ModelSerializer):

    email = serializers.CharField(
        default='default@default.default',
        initial='default@default.default')
    full_name = serializers.CharField(
        default='default_name',
        initial='default_name')
    telegram_name = serializers.CharField(
        default='default_telegram',
        initial='default_telegram')
    username = serializers.CharField(
        default='default_username',
        initial='default_username')

    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'telegram_name', 'username']

    def update(self, instance, validated_data):

        new_email = validated_data.pop('email', None)
        if new_email is not None:
            instance.email = new_email

        new_full_name = validated_data.pop('full_name', None)
        if new_full_name is not None:
            instance.full_name = new_full_name

        new_telegram_name = validated_data.pop('telegram_name', None)
        if new_telegram_name is not None:
            instance.telegram_name = new_telegram_name

        new_user_name = validated_data.pop('username', None)
        if new_user_name is not None:
            instance.username = new_user_name

        instance.save()

        return instance


class CreateOrganizationSerialize(serializers.ModelSerializer):

    class Meta:
        model = Organization
        exclude = ('creation_date', 'admin_id')


class OrganizationSerialize(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ['name', 'description', 'creation_date', 'admin_id']
        read_only_fields = [
            # 'participants',
            'creation_date',
            'admin_id']


class CreateProjectSerialize(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'name']
