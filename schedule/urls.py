from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'timetable.views.home', name='home'),
    url(r'^accounts/', include('registration.urls', namespace='registration')),
    url(r'^schedule/', include('timetable.urls', namespace='employee_schedule')),
    url(r'^messageboard/', include('messageboard.urls', namespace='messageboard')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
