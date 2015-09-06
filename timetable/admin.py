from django.contrib import admin
from timetable.models import Employee, Work, Employer, WorkRequest, WorkPosition
# Register your models here.
class workInline(admin.TabularInline):
    model=Work
    extra=3
    
class EmployeeAdmin(admin.ModelAdmin):
    inlines=[workInline]

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Employer)
admin.site.register(WorkRequest)
admin.site.register(WorkPosition)
admin.site.register(Work)