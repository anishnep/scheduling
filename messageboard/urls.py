from django.conf.urls import patterns , url
from messageboard import views

urlpatterns= patterns('',
    url(r'^messages/$', views.message_list, name="messages"),
    url(r'^create_post/$', views.create_post, name="create_post"),
    url(r'^add_comment/$', views.add_comment, name="add_comment"),
    )
