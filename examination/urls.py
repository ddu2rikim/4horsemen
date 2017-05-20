from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.examination_list, name='examination_list'),
	url(r'^(?P<pk>\d+)/$', views.examination_detail, name='examination_detail'),
	url(r'^new/$', views.examination_new, name='examination_new'),
	url(r'^(?P<examination_pk>\d+)/examination/(?P<pk>\d+)/edit/$', views.examination_edit, name='examination_edit'),
	url(r'^(?P<examination_pk>\d+)/examination/(?P<pk>\d+)/delete/$', views.examination_delete, name='examination_delete'),
	url(r'^(?P<examination_pk>\d+)/examination/(?P<pk>\d+)/transfer/$', views.examination_transfer, name='examination_transfer'),
 ]