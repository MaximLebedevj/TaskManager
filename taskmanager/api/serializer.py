from rest_framework import serializers

from .models import User

from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator


class UserRegisterSerialize(serializers.ModelSerializer):

    password1 = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'full_name', 'password1', 'password2']

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})

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
        fields = ('email', 'password')


class UserLogoutSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class UserSerializeProfile(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'full_name', 'email', 'password', 'telegram_name']

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
