from django.contrib.auth.models import User
from rest_framework import serializers

from userinfo.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.Field(source='get_full_name')
    alerts = serializers.PrimaryKeyRelatedField(many=True,
                                                read_only=True)

    class Meta:
        model = User
        fields = ('id', 'last_login', 'username', 'first_name', 'last_name',
                  'email', 'full_name')
        read_only_fields = ('last_login',)


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=75)
    email = serializers.EmailField(required=True, max_length=75)
    password = serializers.CharField(required=True, max_length=50)
    first_name = serializers.CharField(required=True, max_length=30)
    last_name = serializers.CharField(required=True, max_length=30)


