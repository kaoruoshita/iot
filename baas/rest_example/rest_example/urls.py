"""rest_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
#from django.contrib import admin

#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#]



#from django.conf.urls import patterns, include, url
from django.contrib import admin

from restapp import views
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^emails', views.SendEmails.as_view()),
    url(r'^power', views.DevicePower.as_view()),
    url(r'^photo', views.GetDevicePhoto.as_view()),
    url(r'^state/(?P<pk>[0-9]+)/$', views.GetDeviceState.as_view()),
    url(r'^$', views.index, name='index'),
    url(r'^get_alarms', views.GetAlarms.as_view()),
]

#urlpatterns = patterns('',
#url(r'^admin/', include(admin.site.urls)),
#url(r'^users/', views.UserList.as_view()),
#url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
#),

