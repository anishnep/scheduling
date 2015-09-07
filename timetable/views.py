import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.html import mark_safe
from schedulecalendar.schedule import ScheduleCalendar
from timetable.models import Work, WorkRequest
from employer.models import Employer, Employee




year = datetime.datetime.now().year
month = datetime.datetime.now().month

def home(request):
    
    return render(request, 'frontpage.html', {})

@login_required
def dashboard(request):
    myday = datetime.datetime.now()
    y, m = myday.year, myday.month
    return render(request, 'base.html',{'year':y, 'month':m})

@login_required
def userpage(request):
    if not request.user.is_employer:
        if not request.user.employee.is_supervisor:
            return HttpResponseRedirect('/schedule/dashboard')
    
        
def calendar(request, cal_year=datetime.datetime.now().year, cal_month=datetime.datetime.now().month):
    try:
        #emp=get_object_or_404(request.user.employee)
        emp = request.user.employee
        
    except Employee.DoesNotExist:
        return HttpResponse("Sorry, you are not a valid employee.")
    
    curr_year,curr_month=int(cal_year),int(cal_month)
    prev_year=curr_year
    prev_month=curr_month-1
    if prev_month==0:
        prev_month=12
        prev_year=prev_year-1
    #next_year=curr_year+1
    next_year=curr_year
    next_month=curr_month+1
    if next_month==13:
        next_month=1
        next_year=curr_year+1
    yearafterthis=curr_year+1
    yearbeforethis=curr_year-1
    
    work_day_list=emp.work_set.all().order_by('work_date').filter(work_date__year=cal_year,
                                                              work_date__month=cal_month)
    
    schedule=ScheduleCalendar(work_day_list)
    cal=schedule.formatmonth(int(cal_year),int(cal_month))
    
    return render(request,'timetable/calendar.html', {'calendar':mark_safe(cal),
                                                     'emp': emp,
                                                     'lyear': curr_year,
                                                     'lmonth': curr_month,
                                                     'PreviousYear': prev_year,
                                                     'Nextyear': next_year,
                                                     'PreviousMonth': prev_month,
                                                     'NextMonth': next_month,
                                                     'YearAfterThis': yearafterthis,
                                                     'YearBeforeThis': yearbeforethis,
                                                     })

def day_view(request, cal_year, cal_month, cal_day):
    emp = request.user.employee
    try:
        work_obj = Work.objects.get(employee=emp, work_date__year=cal_year, work_date__month=cal_month,
                                work_date__day=cal_day)
    except Work.DoesNotExist:
        work_obj=None
        
    if work_obj: published = True
    else: published = False
    
    return render(request, 'timetable/day_view.html', {'work_obj':work_obj, 
                                                        'emp':emp, 
                                                        'published':published,
                                                        'year': cal_year,
                                                        'month': cal_month,
                                                        'day': cal_day })
   
def ajax_day_view(request):
    
    if request.method == "GET":
        emp= request.user.employee
        y = int(request.GET["year"])
        m = int(request.GET["month"])
        d = int(request.GET["day"])
        
        try:
            work_obj = Work.objects.get(employee=emp, work_date__year=y, work_date__month=m,
                                work_date__day=d)
        except Work.DoesNotExist:
            work_obj = None
        
        try:
            work_request_object=WorkRequest.objects.get(requested_by=request.user, request_date=datetime.date(y,m,d), checked=False)
        except WorkRequest.DoesNotExist:
            work_request_object=None
            
        return render(request, 'timetable/day_view.html', {'work_obj':work_obj,
                                                        'work_request_object':work_request_object,
                                                        'emp':emp, 
                                                        'year': y,
                                                        'month': m,
                                                        'day': d })
        
def myrequest(request):
    if request.method == "POST":
        request_date = request.POST.get('request_date',None)
        request_type= request.POST.get('request_type',None) #work request type..
        print request_date
        print request_type
        if request_date and request_type:
            d = request_date.split("/") # split the date so as to get year month and day
            y, m, d= int(d[0]), int(d[1]), int(d[2])
            
            if request_type == "workday":
                WorkRequest.objects.get_or_create(
                        requested_by = request.user,
                        request_date = datetime.date(y, m, d),
                        request_type = 1,
                    )  
            elif request_type=="freeday":
                WorkRequest.objects.get_or_create(
                        requested_by = request.user,
                        request_date = datetime.date(y, m, d),
                        request_type = 2,
                        )
        return HttpResponse("Your Request has been sent for approval")
    return HttpResponse("NOT POSSIBLE")
    
    
def testpage(request):
    return HttpResponse("TEst page call")
