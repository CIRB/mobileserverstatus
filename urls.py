from django.conf.urls.defaults import url, patterns

from mobileserverstatus.views import get_status

urlpatterns = patterns('mobileserverstatus.views',
    url(r'^$', 'get_status'),
)
