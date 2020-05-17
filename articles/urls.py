from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name='list'),
    url(r'^about/$', views.article_list),
    url(r'^(?P<slug>[\w-]+)/$', views.article_details, name='details'),

]
