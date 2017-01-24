from django.conf.urls import urls
from . import views

urlpatterns = [
	url(r'^apply/$', views.coupon_apply, name='apply'),
]