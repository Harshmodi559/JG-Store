from django.contrib import admin
from django.urls import path,include

from JGS import views as store
from api import views as Api
urlpatterns = [
    path('admin/', admin.site.urls),



    path('',store.splash,name="splash"),
    path('dashboard/',store.home,name="dashboard"),
    path('insert/',store.insert_data,name="insert"),
    path('fetch/',store.fetch,name="fetch"),
    path('api/',Api.api,name="api"),
    path('api/<int:id>',Api.api,name="api_by_id"),

]
