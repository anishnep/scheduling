import xlrd
import datetime

class Excel_Upload:
    def __init__(self,content):
        self.content=content
        
    def load_workbook(self):
        #C:\\Users\\Anish\\Desktop\\venv\\src\\timetable\\Book2.xls
        wb=xlrd.open_workbook(file_contents=self.content)
        sheet=wb.sheet_by_name('Sheet1')
        return sheet
    
    def get_employee_dict(self):
        sheet=self.load_workbook()
              
        emp_id=sheet.col_values(0)
        emp_name=sheet.col_values(1)
        
        emp_dict=dict(zip(emp_id,emp_name))
        return emp_dict
    
    def get_work_dict(self,employee_id):
        sheet=self.load_workbook()      
        work_dict={}
         #iterate through each row starting from row 13: our data starts from row 13
        for row in range(13,sheet.nrows):
            #extract id and name from the sheet. column 0 has id and column 1 has name
            
            emp_id=sheet.cell_value(row,0)
            emp_name=sheet.cell_value(row,1)
            
            if employee_id==emp_id and emp_name:
                
                #create a dictionary for mapping id and name if there are any found in a row
                
                #employee=dict(zip(emp_id,emp_name))
                for col in range(2,sheet.ncols):
                    #3 rows belong to each employee, extract all the rows that belong to each employee by each column
                    data=sheet.col_values(col,row,row+3)
                    #dt=sheet.cell_value(8,col)
                    
                                       
                    if sheet.cell_type(8,col)==xlrd.XL_CELL_DATE:
                        y,m,d=xlrd.xldate_as_tuple(sheet.cell_value(8,col),0)[:3]
                        date=datetime.date(y,m,d)
                    
                        if any(data):
                            for item in data:
                                if item:
                                    work_dict[date]=item

                                                    
                        if not any(data):
                            
                            work_dict[date]=0
                        #print(sheet.cell_value(8,col))
                           
        if not len(work_dict):
            print('No record found')
           
        return work_dict


    
   
        
        
    
        
        
        
        
        
    
