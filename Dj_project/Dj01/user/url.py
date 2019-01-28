from django.contrib import admin
from django.conf.urls import url
from django.urls import path
#引入视图文件
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^username/$',views.username)
]