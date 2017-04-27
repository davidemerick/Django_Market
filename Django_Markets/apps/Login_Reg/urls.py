from django.conf.urls import url
from . import views           # So we can call functions from our routes!
urlpatterns = [
	url(r'^$', views.index, name = 'render_index'),       # 'home' route.
	url(r'^register', views.register, name='process_register'),
	url(r'^login', views.login, name='process_login'),
	url(r'^home', views.renderSuccessfulLogin, name='render_auth'),
	url(r'^logout', views.process_logout, name='process_logout'),
]
