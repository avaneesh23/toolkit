from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from settings import INSTALLED_APPS


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'handsontable.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

 # apps
if 'userinfo' in INSTALLED_APPS:
    urlpatterns += patterns('',url(r'^', include('userinfo.urls')))
if 'website' in INSTALLED_APPS:
    urlpatterns += patterns('', url(r'^', include('website.urls')))

# Rest framework login
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)
