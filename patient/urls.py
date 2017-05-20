from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.patient_list, name='patient_list'),
	url(r'^(?P<pk>\d+)/$', views.patient_detail, name='patient_detail'),
	url(r'^new/$', views.patient_new, name='patient_new'),
	url(r'^(?P<patient_pk>\d+)/patient/(?P<pk>\d+)/edit/$', views.patient_edit, name='patient_edit'),
	url(r'^(?P<patient_pk>\d+)/patient/(?P<pk>\d+)/delete/$', views.patient_delete, name='patient_delete'),
]