import csv
import random
from dataclasses import dataclass

@dataclass
class Student:
    firstName: str
    lastName: str
    tableAssigned: str
# Student Class 

kitchenCrew = []
#Kitchen Crew Array
tables = []
#Tables Array
tableNumber = 1
#Table Number Variable
studentArray = [[] for i in range(0,32)]
#Student Array
studentArrayTwo =[]
waitersArray = []
for x in range(0,290): 
    if x < 31:
        tables.append(str(tableNumber) + 'w')                   
        tableNumber +=1
    else:
        if tableNumber < 32:
            tables.append(str(tableNumber))                   
            tableNumber +=1
        else:
            tables.append('Kitchen Crew')
            tableNumber = 1
random.shuffle(tables)
#Creates an array of tables

 
  
with open('Dinner Seating - Student List 2018-19.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader: 
            if tables[line_count] == 'Kitchen Crew':
                kitchenCrew.append(Student(row[1], row[0], tables[line_count]))
            else:
                for x in range(0,32):
                    if (str(x)) == tables[line_count]:  
                        studentArray[x].append(Student(row[1],row[0],tables[line_count]))
                    if (str(x) + 'w') == tables[line_count]:     
                        waitersArray.append(Student(row[1],row[0],tables[line_count]))
            line_count += 1
for x in range(1,32):
    print('table' + str(x))
    print(studentArray[x])
    print('-------------------------------------------------')
print('Kitchen Crew')
print(kitchenCrew)
print('Waiters')
print(waitersArray)
#Assigns each student Last Name, First Name to a table from randomized table array. Separates into tables in kitchen crew 
