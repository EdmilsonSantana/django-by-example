from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	# account views
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^register/', views.register, name='register'),
	url(r'^edit/$', views.edit, name='edit'),

	# login / logout urls
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, name='logout'),
	url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout-then-login'),

	# change password urls
	url(r'^password-change/$', auth_views.password_change, name='password_change'),
	url(r'^password-change/done/$', auth_views.password_change_done, name='password_change_done'),

	# restore password urls
	url(r'^password-reset/$', auth_views.password_reset, name='password_reset'),
	url(r'^password-reset/done$', auth_views.password_reset_done, name='password_reset_done'),
	url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
	url(r'^password-reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),

	# user profiles
	url(r'^users/$', views.user_list, name='user_list'),
	url(r'^users/follow/$', views.user_follow, name='user_follow'),
	url(r'^users/(?P<username>[-\w]+)/$', views.user_detail, name='user_detail'),

]