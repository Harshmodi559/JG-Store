from django.contrib import admin
from django.urls import path, include

from JGS import views as store
from api import views as Api

from django.views.static import serve
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', store.splash, name="splash"),
    path('dashboard/', store.home, name="dashboard"),
    path('insert/', store.insert_data, name="insert"),
    path('fetch/', store.fetch, name="fetch"),
    path('fetch/<int:pk>', store.fetch, name="fetch_by_id"),
    path('api/', Api.api, name="api"),
    path('api/<int:id>', Api.api, name="api_by_id"),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

