from django.conf.urls import patterns, include, url
from timetable import views

employer_url = patterns('',
        url(r'^testpage/$', views.testpage)
        
    )


urlpatterns= patterns('',
        url(r'^userpage/$', views.userpage, name="userpage"),
        url(r'^dashboard/$', views.dashboard, name="dashboard"),
        url(r'^cal/(?P<cal_year>\d+)/(?P<cal_month>\d+)/$', views.calendar, name="calendar"),
        url(r'^cal/(?P<cal_year>\d+)/(?P<cal_month>\d+)/(?P<cal_day>\d+)/$', views.day_view, name="day_view"),
        url(r'^ajax_day_view/$', views.ajax_day_view, name="ajax_day_view"),
        url(r'^myrequest/$', views.myrequest, name="myrequest"),
        url(r'^employer/',include(employer_url)),
    )
