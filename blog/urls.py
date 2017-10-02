from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',view.post_list,name='post_list'),
    url(r'^post/(?<pk>[0-9]+)/$',views.post_detail,name='post_detail'),
]
