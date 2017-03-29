from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^users/(?P<id>\d+)$', views.info, name='info'),
	url(r'^create$', views.create, name='create'),
	url(r'^fav/(?P<id>\d+)$', views.fav, name='fav'),
	url(r'^delelte/(?P<id>\d+)$', views.delete, name='delete'),


]