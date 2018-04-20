from django.conf.urls import include, url
from django.contrib import admin

from .views import *
from .models import Album, Photo

urlpatterns = [
    url(r'^$', AlbumLV.as_view(), name='index'),
    url(r'^album/$', AlbumLV.as_view(), name='album_list'),
    url(r'^album/(?P<pk>\d+)/$', AlbumDV.as_view(), name='album_detail'),
    url(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(), name='photo_detail'),

    url(r'^admin/', admin.site.urls),

    # path : /photo/id/
    url(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(), name='photo_detail'),


    # path : /album/add/
    url(r'^album/add/$', AlbumPhotoCV.as_view(), name='album_add'),

    # path : /album/change/
    url(r'^album/change/$', AlbumChangeLV.as_view(), name='album_change'),

    # path : /album/id/update/
    url(r'^album/(?P<pk>\d+)/update/$', AlbumPhotoUV.as_view(), name='album_update'),

    # path : /album/id/delete/
    url(r'^album/(?P<pk>\d+)/delete/$', AlbumDeleteView.as_view(), name='album_delete'),


    # path : /photo/add/
    url(r'^photo/add/$', PhotoCreateView.as_view(), name='photo_add'),

    # path : /photo/chage/
    url(r'^photo/change/$', PhotoChangeLV.as_view(), name='photo_change'),

    # path : /photo/id/update/
    url(r'^photo/(?P<pk>\d+)/update/$', PhotoUpdateView.as_view(), name='photo_update'),

    # path : /photo/id/delete/
    url(r'^photo/(?P<pk>\d+)/delete/$', PhotoDeleteView.as_view(), name='photo_delete'),

]
