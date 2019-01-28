
from django.conf.urls import url
#引入视图文件
from .import views
urlpatterns = [
    url(r'^laora/$',views.laora)
]