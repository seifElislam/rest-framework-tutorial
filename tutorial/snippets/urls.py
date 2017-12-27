from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'^snippets/$', snippet_list),
    url(r'^snipprts/(?P<pk>[0-9]+)/$', snippet_details)
]