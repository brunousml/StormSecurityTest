from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^filme/(?P<slug>[\w-]+)/$', views.movie, name='movie'),
    url(r'^ator/(?P<actor_name>[\w-]+)/$', views.order_by_actor, name='order_by_actor'),
    url(r'^(?P<slug>[\w-]+)/$', views.order_by_gender, name='order_by_gender'),
]
