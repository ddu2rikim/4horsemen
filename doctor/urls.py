from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.doctor_list, name='doctor_list'),
	url(r'^(?P<pk>\d+)/$', views.doctor_detail, name='doctor_detail'),
	url(r'^new/$', views.doctor_new, name='doctor_new'),
	url(r'^(?P<doctor_pk>\d+)/doctor/(?P<pk>\d+)/edit/$', views.doctor_edit, name='doctor_edit'),
	url(r'^(?P<doctor_pk>\d+)/doctor/(?P<pk>\d+)/delete/$', views.doctor_delete, name='doctor_delete'),
]