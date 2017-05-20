from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.appointment_list, name='appointment_list'),

	url(r'^(?P<pk>\d+)/$', views.appointment_detail, name='appointment_detail'),

	url(r'^new/$', views.appointment_new, name='appointment_new'),

	url(r'^(?P<appointment_pk>\d+)/appointment/(?P<pk>\d+)/edit/$', views.appointment_edit, name='appointment_edit'),

	url(r'^(?P<appointment_pk>\d+)/appointment/(?P<pk>\d+)/delete/$', views.appointment_delete, name='appointment_delete'),
]