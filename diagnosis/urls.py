from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.diagnosis_list, name='diagnosis_list'),
	url(r'^(?P<pk>\d+)/$', views.diagnosis_detail, name='diagnosis_detail'),
	url(r'^new/$', views.diagnosis_new, name='diagnosis_new'),
	url(r'^(?P<diagnosis_pk>\d+)/diagnosis/(?P<pk>\d+)/edit/$', views.diagnosis_edit, name='diagnosis_edit'),
	url(r'^(?P<diagnosis_pk>\d+)/diagnosis/(?P<pk>\d+)/delete/$', views.diagnosis_delete, name='diagnosis_delete'),
	url(r'^(?P<diagnosis_pk>\d+)/diagnosis/(?P<pk>\d+)/transfer/$', views.diagnosis_transfer, name='diagnosis_transfer'),
    url(r'^(?P<diagnosis_pk>\d+)/diagnosis/(?P<pk>\d+)/transfer/$', views.diagnosis_edit, name='sendingPrescription'),

 ]