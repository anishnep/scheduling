from django.conf.urls import patterns, url

urlpatterns = patterns('',
                   #url(r'^register/$', views.register, name='register'),
                   url(r'^login/$','django.contrib.auth.views.login', name='login'),
                   url(r'^logout/$','django.contrib.auth.views.logout',{'next_page':'/accounts/login/'}, name='logout'),
                     )
