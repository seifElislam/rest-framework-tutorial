from django.conf.urls import url, include
from views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter


snippet_list = SnippetViewSet.as_view({'get': 'list', 'post': 'create'})
snippet_details = SnippetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch':
    'partial_update', 'delete': 'destory'})
snippet_highlight = SnippetViewSet.as_view({'get': 'highlight'}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_details = UserViewSet.as_view({
    'get': 'retrieve'
})

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    # for function based views
    # url(r'^snippets/$', snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_details)
    # for class based views
    # url(r'^snippets/$', SnippetList.as_view(), name='snippet-list'),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetails.as_view(), name='snippet-detail'),
    # url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', SnippetHighlight.as_view(), name='snippet-highlight'),
    # user end-points
    # url(r'^users/$', UserList.as_view(), name='user-list'),
    # url(r'^users/(?P<pk>[0-9]+)/$', UserDetails.as_view(), name='user-detail'),
    # root api
    # url(r'^$', api_root),
    # viewsets views without router
    # url(r'^snippets/$', snippet_list, name='snippet-list'),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_details, name='snippet-detail'),
    # url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
    # url(r'^users/$', user_list, name='user-list'),
    # url(r'^users/(?P<pk>[0-9]+)/$', user_details, name='user-detail')
    # viewsets views using router
    url(r'^', include(router.urls))
]


# urlpatterns = format_suffix_patterns(urlpatterns)