"""PVTSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from PVTSystem import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^appointment/', include('appointment.urls', namespace='appointment')),
    url(r'^patient/', include('patient.urls', namespace='patient')),
    url(r'^doctor/', include('doctor.urls', namespace='doctor')),
    url(r'^examination/', include('examination.urls', namespace='examination')),
    url(r'^diagnosis/', include('diagnosis.urls', namespace='diagnosis')),
    url(r'^account/', include('accounts.urls')),
    #url(r'^accounts/logout/', auth_views.logout, name='logout', kwargs={'next_page': settings.LOGIN_URL,}),
    url(r'^login/', include('accounts.urls', namespace='login')),
]
