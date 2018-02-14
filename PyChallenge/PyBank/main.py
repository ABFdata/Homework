
# coding: utf-8

# In[106]:

# read csv_file1

import csv

with open('budget_data_1.csv', 'r') as csv_file1:
    csv_reader1 = csv.reader(csv_file1)
    
    # use to skip header in col
    next(csv_reader1)
    
    # set empty list for month_list1 to store months from col 1
    month_list1 = []
    
    # set empty list for revenue_list1 to store rev from col 2
    revenue_list1 = []
    
    prev_rev = 0
    month_of_change = []
    rev_change_list = []
    total_rev = 0
    
    for col in csv_reader1:
        
        # append col 1 months to month_list1
        month_list1.append(col[0])
        
        #append col 2 rev to revenue_list2
        revenue_list1.append(int(col[1]))
        
        # rev change
        rev_change = int(col[1]) - prev_rev
        prev_rev = int(col[1])
        rev_change_list = rev_change_list + [rev_change]
        month_of_change = month_of_change + [col[0]]
        
        # store the length of month_list1 to a variable 
        total_months1 = len(month_list1)
        


# In[107]:

# find the sum of RevenueTotal_1
RevenueTotal_1 = 0 

# Loop 0 to the number of items in the revenue_list1
for i in range(len(revenue_list1)):
    # add index 0, next 1, etc
    RevenueTotal_1 += int(revenue_list1[i]) 



# In[108]:

# store the length of month_list1 to a variable 
# total_months1 = len(month_list1)


# In[109]:

# find max revenue in revenue_list1
MaxRev1 = max(revenue_list1) 


# In[110]:

# find the index of MaxRev 1 to match to the month index
for i, j in enumerate(revenue_list1):
    if j == MaxRev1:
        print (i) 
        GreatMonth = month_list1[i] # pass i through index to get month
        print(GreatMonth)


# In[111]:

# find min revenue in revenue_list1
MinRev1 = min(revenue_list1)


# In[112]:

# Avg Rev Change

rev_avg = sum(rev_change_list) / len(rev_change_list)
print(rev_avg)
rev_avg1_round = round(rev_avg,2)
print(rev_avg1_round)


# In[113]:

# read csv_file2

with open('budget_data_2.csv', 'r') as csv_file2:
    csv_reader2 = csv.reader(csv_file2)
    
    next(csv_reader2)
    
    month_list2 = []
    
    revenue_list2 = []
    
    prev_rev2 = 0
    month_of_change2 = []
    rev_change_list2 = []
    total_rev2 = 0
    
    for col in csv_reader2:
        
        # append col 1 in budget_data_2 to month_list2
        month_list2.append(col[0])
        
        # append col 2 in budget_data_2 to revenue_list2
        revenue_list2.append(int(col[1]))
        
        # rev change
        rev_change2 = int(col[1]) - prev_rev2
        prev_rev2 = int(col[1])
        rev_change_list2 = rev_change_list2 + [rev_change2]
        month_of_change2 = month_of_change2 + [col[0]]


# In[114]:

# find the sum of revenue_list2
RevenueTotal_2 = 0

# Loop 0 to the number of items in revenue_list2
for j in range(len(revenue_list2)):
    RevenueTotal_2 += int(revenue_list2[j]) 
    


# In[115]:

# store the length of month_list2 to a new variable 
total_months2 = len(month_list2)


# In[116]:

# find Max Revenue in revenue_list2
MaxRev2 = max(revenue_list2)


# In[117]:

# find Min Revenue in revenue_list2
MinRev2 = min(revenue_list2)


# In[118]:

# find index of MinRev2
for i, j in enumerate(revenue_list2):
    if j == MinRev2:
        # print (i)
        DecMonth = month_list2[i]
        print(DecMonth)  


# In[119]:

# Use if statement to find Greatest_Increase

if MaxRev1 > MaxRev2:
    Greatest_Increase = MaxRev1
else:
    Greatest_Increase = MaxRev2

print('Greatest Increase: ' + str(Greatest_Increase))

# Use if statement to find Greatest_Decrease

if MinRev1 > MinRev2:
    Greatest_Decrease = MinRev1
else:
    Greatest_Decrease = MinRev2

print('Greatest Decrease: ' + str(Greatest_Decrease))


# In[120]:

# Avg Rev Change

rev_avg2 = sum(rev_change_list2) / len(rev_change_list2)
print(rev_avg2)

rev_avg2_round = round(rev_avg2,2)
print(rev_avg2_round)


# In[121]:

# SOLUTIONS

print("Financial Analysis")
print('----------------------------------')

# Add total_months1 to total_months2
TotalMonths = total_months1 + total_months2 # -------------------------------- TotalMonths
print("Total Months: " + str(TotalMonths))

TotalRevenue = RevenueTotal_1 + RevenueTotal_2
print("Total Revenue: " + "$" + str(TotalRevenue))

# Average Revenue Change
print("Average Revenue Change: " + "$" + str(rev_avg1_round))

# Greatest Increase in Revenue
print("Greatest Increase in Revenue: " + str(GreatMonth) + " " + "($" + str(Greatest_Increase) + ")")

# Greatest Decrease in Revenue
print("Greatest Decrease in Revenue: " + str(DecMonth) + " " +  "($" + str(Greatest_Decrease) + ")")
    

