from django.shortcuts import render
from employer.models import Employee, Employer
from django.views.generic import ListView, DetailView


class EmployeeList(ListView):
    context_object_name = "employee_list"
    template_name = "employer/employee_list.html"
    
    def get_queryset(self):
        self.employer = self.request.user.employer
        return Employee.objects.filter(employer = self.employer)
    
    