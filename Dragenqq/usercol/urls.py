from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^myblog/$', views.myblog, name='myblog'),
    url(r'^whisper/$', views.whisper, name='whisper'),
    url(r'^leacots/$', views.leacots, name='leacots'),
    url(r'^album/$', views.album, name='album'),
    url(r'^about/$', views.about, name='about'),
    url(r'^my/$', views.my, name='my'),
    url(r'^friendmanage/$', views.friendmanage, name='friendmanage'),
    url(r'^details/$', views.details, name='details'),
    url(r'^register/$', views.register, name='register'),
    url(r'^userinfo/$', views.login, name='userinfo'),
    url(r'^update/$', views.update, name='update'),
    url(r'^addone/$', views.addone, name='addone'),
    url(r'^(\d+)/article/$', views.article, name='article'),
    url(r'^writing/$', views.writing, name='writing'),
    url(r'^yanzheng/$', views.yanzheng, name='yanzheng'),
    url(r'^artupdate/$', views.artupdate, name='artupdate'),
    url(r'^reg/$', views.reg, name='reg'),
    url(r'^delinfo/$', views.delinfo, name='delinfo'),
    url(r'^quit/$', views.quit, name='quit'),
    url(r'^.*$', views.index, name='index'),
]