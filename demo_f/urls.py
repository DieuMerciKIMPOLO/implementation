"""

"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from demo import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^o/authorize/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
	url(r'^demof/', include('demo.urls')),
]
