from calendar import HTMLCalendar
import datetime

#this function iterate over each week of a month and get the first day of that week.
def get_usable_day(week):
    for d,wd in week:
            if d:
                day=d
                break;
    return day
    
class ScheduleCalendar(HTMLCalendar):
    
    def __init__(self,emp_work_list):
        super(ScheduleCalendar,self).__init__()
        self.emp_work_list=emp_work_list
        

    def formatday(self,day,weekday):
        self.day=day
        today=datetime.date.today()
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if datetime.date(self.year,self.month,day) == today:
                cssclass= 'today'
            if self.emp_work_list.count() > 0:
                             
                body = []
            
                for workday in self.emp_work_list:
                    
                    if (workday.work_date.year,workday.work_date.month,workday.work_date.day) == (self.year,self.month,day):
                        if workday.has_work == True:
                            cssclass += ' workday'
                        

                        elif workday.has_work == False:
                            cssclass += ' noworkday'
                            
                #return self.day_cell(cssclass = cssclass, link = '%d/'%day, body = "%d %s"%(day,''.join(body))) #revert to this if problem
                return self.day_cell(cssclass = cssclass, link = '', body = "%d %s"%(day,''.join(body)))#changed code...(17.7.2015)
                
            #(original)return self.day_cell(cssclass=cssclass,link='%d/'%day,body=int(day))
            #return self.day_cell(cssclass=cssclass,link='%d/'%day,body=int(day)) #revert to this if problem
            
            return self.day_cell(cssclass=cssclass,link='', body=int(day))#changed code...(17.7.2015)
        return self.day_cell('noday','','&nbsp;')
        
    def day_cell(self,cssclass,link,body):
        if link:
            
            #(original)return '<td class="%s"><a href="%s">%s</a></td>' % (cssclass,link, body)
            
            return '<td class="%s" data-year="%d" data-month="%d">"%s %s"</td>'%(cssclass,self.year, self.month,link,body) #changed code....(17.7.2015)
            #return '<td class="%s" onClick=\'parent.location="%s"\'>%s</td>' %(cssclass,link, body)
        return '<td class="%s" data-year="%d" data-month="%d">%s</td>' % (cssclass,self.year, self.month, body)
        
    def formatweek(self, theweek):
        day=get_usable_day(theweek) 
        print (day)
        dt=datetime.date(self.year,self.month,day).isocalendar()[1]
        s = ''.join(self.formatday(d, wd) for (d, wd) in theweek)
        
        return '<tr class="week week-%d">%s</tr>'%(dt,s) 
        
    def formatmonth(self, year, month):
        self.year,self.month=year,month
        return super(ScheduleCalendar,self).formatmonth(year,month)

