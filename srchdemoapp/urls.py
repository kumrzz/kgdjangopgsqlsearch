from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^mktsearch/$', views.all_listings, name='mktsearch'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.all_listings, name='listings_by_category'),
    url(r'^$', views.all_listings, name='srchdemoapp_main'),
]
