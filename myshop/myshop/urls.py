"""myshop URL Configuration

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
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from shop import urls as shop_urls
from cart import urls as cart_urls
from orders import urls as orders_urls
from payment import urls as payment_urls
from coupons import urls as coupons_urls

from paypal.standard.ipn import urls as paypal_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include(cart_urls, namespace='cart')),
    url(r'^orders/', include(orders_urls, namespace='orders')),
    url(r'^paypal/', include(paypal_urls)),
    url(r'^payment/', include(payment_urls, namespace='payment')),
    url(r'^coupons/', include(coupons_urls, namespace='coupons')),
    url(r'^', include(shop_urls, namespace='shop')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)