from django.conf.urls import url, include, patterns
from employer import views

urlpatterns = patterns('',
    url(r'^employees/$', views.EmployeeList.as_view(), name = "employee_list"),
    )