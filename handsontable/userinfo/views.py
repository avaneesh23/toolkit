
# Create your views here.
import json
import logging
import requests
import warnings

from django.http import Http404
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.db import connections
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics
from rest_framework import permissions
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from userinfo.models import UserInfo
from userinfo.serializers import UserInfoSerializer
from userinfo.serializers import UserRegistrationSerializer
from userinfo.serializers import UserSerializer


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
warnings.simplefilter('always', DeprecationWarning)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Endpoint : /userinfo/
    """
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        queryset = self.get_queryset()
        upk = self.kwargs.get('upk')
        if upk:
            userid = int(upk)
        else:
            # Deprecated support for old enpoints
            warnings.warn("userid GET param will be removed in v1.0 release",
                     DeprecationWarning)
            userid = self.request.GET.get('userid', self.request.user.id)
            if not type(userid) == int and not str(userid).isdigit():
                raise Http404
        obj = get_object_or_404(queryset, pk=userid)
        return obj

    def get_queryset(self):
        user = self.request.user
        if str(user) == 'euprime':
            return User.objects.all()
        else:
            queryset = User.objects.filter(pk=user.id)
            for org in user.extra_info.organizations.all():
                queryset = queryset | User.objects.filter(
                        extra_info__organizations=org)
            return queryset


class UserRegistrationDuplicateError(APIException):
    status_code = 400
    default_detail = 'Username already taken.'


class UserRegistration(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serialized = UserRegistrationSerializer(data=request.DATA)
        if serialized.is_valid():
            user, ret = User.objects.get_or_create(
                username=serialized.init_data['username'],
                defaults={
                    'email': serialized.init_data['email'],
                    'first_name': serialized.init_data['first_name'],
                    'last_name': serialized.init_data['last_name']
                }
            )
            if not ret:
                logger.info("User registration failed due to duplicate, " + \
                            "returning 400: {}".format(serialized.init_data))
                raise UserRegistrationDuplicateError
            user.set_password(serialized.init_data['password'])
            user.save()
            logger.info("User registration successful, " + \
                        "returning 201: {}".format(serialized.data))
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            logger.info("User registration failed serializer check, " + \
                        "returning 400: {}".format(serialized._errors))
            return Response(serialized._errors,
                status=status.HTTP_400_BAD_REQUEST)


class UserInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Endpoint : /userinfo/owner_id
    """
    serializer_class = UserInfoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        user = self.request.user
        upk = self.kwargs.get('upk')
        if str(user) == 'euprime':
            if upk:
                userid = int(upk)
            else:
                # Deprecated support for old enpoints
                warnings.warn("userid GET param will be removed in v1.0 release",
                              DeprecationWarning)
                userid = self.request.GET.get('userid', self.request.user.id)
                if not type(userid) == int and not str(userid).isdigit(): raise Http404
            user = get_object_or_404(User, pk=userid)
            obj, ret = UserInfo.objects.get_or_create(owner=user)
        else:
            if not upk: upk = user
            obj, ret = UserInfo.objects.get_or_create(owner=upk)
        return obj


