"""wearesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from accounts.views import register, login, profile, logout, subscriptions_webhook, paypal_cancel, paypal_return, \
    all_products
from paypal.standard.ipn import urls as paypal_urls
from products.views import magazines
import core.views
from threads.views import threads
import threads.views
import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', core.views.get_index, name='home'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^contact/', 'contact.views.contact', name='contact'),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^//logout/$', logout, name='logout'),
    url(r'^accounts/subscriptions/$', subscriptions_webhook),
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return/$', paypal_return),
    url(r'^paypal-cancel/$', paypal_cancel),
    url(r'^products/$', all_products, name="products"),
    url(r'^magazines/$', magazines, name="magazines"),

    url(r'^forum/$', threads.views.forum, name="forum"),
    url(r'^threads/(?P<subject_id>\d+)/$', threads.views.threads, name="threads"),
    url(r'^new_thread/(?P<subject_id>\d+)/$', threads.views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', threads.views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', threads.views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', threads.views.edit_post, name='edit_post'),
    url(r'^post/delete_post/(?P<post_id>\d+)/$', threads.views.delete_post, name='delete_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)