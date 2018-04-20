#pytagram/urls.py

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from .views import MainView, UserCreateView, UserCreateDoneTV


urlpatterns = [
    url(r'^$', MainView.as_view(), name='home'),
    url(r'^photo/', include('photos.urls', namespace='photo')),


    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
