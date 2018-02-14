
# coding: utf-8

# In[2]:

# read csv file

import csv 

with open('election_data_2.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # use to skip header 
    next(csv_reader)
    
    # set empty lists for columns
    
    Candidate_List = [] # variable for candidates (finding the candidates in the list)
    Candidate_List_Count = [] # variable for TOTAL VOTES CASTED
    
    for row in csv_reader:
        # append columns to empty lists
        Candidate_List.append(row[2])
        Candidate_List_Count.append(str(row[2]))


# In[3]:

# find complete list of Candidates 
# by using set to parse out duplicates
    
c = Candidate_List
c = list(set(c))
# print (c)

c1 = c[0]
c2 = c[1]
c3 = c[2]
c4 = c[3]


# In[4]:

from collections import Counter

Vote_Dict = dict(Counter(Candidate_List_Count))

# print(Vote_Dict)

Li_Count = []
O_Tooley_Count = []
Khan_Count = []
Correy_Count = []

Li_Count = (Vote_Dict['Li'])
# print(Li_Count)

O_Tooley_Count = (Vote_Dict["O'Tooley"])
# print(O_Tooley_Count)

Khan_Count = (Vote_Dict['Khan'])
# print(Khan_Count)

Correy_Count = (Vote_Dict['Correy'])
# print(Correy_Count)


# In[6]:

# find the total number of votes by getting the length of Candidate_List
    
Total_Votes_Cast = Li_Count + O_Tooley_Count + Khan_Count + Correy_Count


# In[8]:

# find % of votes for each candidate

Li_percent = (Li_Count / Total_Votes_Cast) * 100
O_Tooley_percent = (O_Tooley_Count / Total_Votes_Cast) * 100
Khan_percent = (Khan_Count / Total_Votes_Cast) * 100
Correy_percent = (Correy_Count / Total_Votes_Cast) * 100


# In[9]:

# SOLUTIONS

print('Election Results')
print('--------------------------------')
print('Total Votes: ' + str(Total_Votes_Cast))
print('--------------------------------')
print(str(c1) + ': ' + str(round(Li_percent,2)) + '% ' + '(' + str(Li_Count) + ')')
print(str(c2) + ': ' + str(round(O_Tooley_percent,2)) + '% ''(' + str(O_Tooley_Count) + ')')
print(str(c3) + ': ' + str(round(Khan_percent,2)) + '% ''(' + str(Khan_Count) + ')')
print(str(c4) + ': ' + str(round(Correy_percent,2)) + '% ''(' + str(Correy_Count) + ')')
print('--------------------------------')
print('Winner: ' + 'Khan')
print('--------------------------------')


# In[ ]:



