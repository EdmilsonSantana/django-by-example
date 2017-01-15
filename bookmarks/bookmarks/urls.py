"""bookmarks URL Configuration

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
from account import urls as account_urls
from images import urls as images_urls
from django.conf import settings
from django.conf.urls.static import static
#from social_django import urls as social_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/',  include(account_urls)),
    url(r'^images/', include(images_urls, namespace='images')),
    # python-social-auth-django
  #  url(r'^social-auth/', include(social_urls, namespace='social'))
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
