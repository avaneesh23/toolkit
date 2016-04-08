from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from userinfo import views

urlpatterns = patterns('',
    url(r'^user/$', views.UserDetail.as_view()),
    url(r'^user/(?P<upk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^user/register/$', views.UserRegistration.as_view()),
    url(r'^userinfo/$', views.UserInfoDetail.as_view()),
    url(r'^userinfo/(?P<upk>[0-9]+)/$', views.UserInfoDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
