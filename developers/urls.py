from django.conf.urls import patterns, include, url
from django.contrib import admin
from.views import * 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import ListView
from .models import *
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from django.contrib.auth import views
from django.contrib.auth import urls


urlpatterns = patterns('',      
    url(r'^$', TemplateView.as_view(template_name='devconnect/index.html'), name='index'),
    url(r'^developers/', developerInfo.as_view(), name="developerinfo"),
    url(r'^developer/(?P<slug>\S+)$', developerDetail.as_view(), name="developer_detail"),
    url(r'^contacts/$','developers.views.contact', name='contacts'),
    url(r'^index/', BlogIndex.as_view(), name="indexs"),
    #url(r'^about/', 'dss.views.about', name="about"),
    url(r'^entry/(?P<slug>\S+)$', BlogDetail.as_view(), name="entry_detail"),
    url(r'^hire/$','developers.views.hire_portal', name='hire'),
    url(r'^profile/$','developers.views.dev_profile', name='profile'),
    url(r'^register/$', 'developers.views.register_user', name='register_user'),
    url(r'^accounts/login/$', 'developers.views.user_login', name='login'),
    url(r'^accounts/logout/', 'developers.views.user_logout', name='loggedout'),
    url(r'^password/$', 'django.contrib.auth.views.password_reset', {}, 'password_reset'),
    url(r'^accounts/password_change/$','django.contrib.auth.views.password_change', 
        {'post_change_redirect' : '/accounts/password_change/done/'}, 
        name="password_change"), 
    url(r'^accounts/password_change/done/$','django.contrib.auth.views.password_change_done'),
    url(r'^accounts/password_reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/accounts/password_reset/mailed/'},
        name="password_reset"),
    url(r'^accounts/password_reset/mailed/$',
        'django.contrib.auth.views.password_reset_done'),
    url(r'^accounts/password_reset/(?P<uidb64>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/accounts/password_reset/complete/'}),
    url(r'^accounts/password_reset/complete/$', 
        'django.contrib.auth.views.password_reset_complete') 
                        
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)