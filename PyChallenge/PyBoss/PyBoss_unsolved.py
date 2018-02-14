
# coding: utf-8

# In[1]:

import csv
from datetime import datetime

# read both csv files


with open ('employee_data1.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # skips header row since we have to edit later
    next(csv_reader)
        
    with open('employee_data2.csv', 'r') as csv_file2:
        csv_reader2 = csv.reader(csv_file2)
        
        next(csv_reader2)
        
        # creates new csv doc     
        with open('employee_data_MERGE.csv', 'w') as new_file1:
            csv_writer = csv.writer(new_file1, delimiter =',')
            
            # write new headers
            csv_writer.writerow(['Emp ID','First Name','Last Name',
                             'DOB','SSN','State'])
        
            # writes employee_data1 to employee_data_MERGE.csv
            for line in csv_reader:
                csv_writer.writerow(line)
                
            # writes employee_data2.csv to employee_data_MERGE.csv
            for line in csv_reader2:
                csv_writer.writerow(line)
            
            


# In[2]:

# read employee_data_MERGE.csv to parse

with open('employee_data_MERGE.csv', 'r') as csv_file3:
    csv_reader3 = csv.reader(csv_file3)
    
    next(csv_reader3)
    
    name_list = []
    first_name_list = []
    last_name_list = []
    DOB_list = []
    SSN_list = []
    State_list = []
    
    
    for row in csv_reader3:
        # row = [Emp ID, Name, DOB, SSN, State]
        
        DOB_list.append(row[2])
        # print(DOB_list)
        # DOB_format = datetime.strptime(row[2], '%d/%m/%Y')
        
        # print(row[4])
        
    


# In[ ]:



