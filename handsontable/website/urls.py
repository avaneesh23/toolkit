from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from website import views

urlpatterns = patterns('',
    url(r'^$', login_required(views.Website.as_view())),
    url(r'^excel/$', login_required(views.Website.as_view())),
)


