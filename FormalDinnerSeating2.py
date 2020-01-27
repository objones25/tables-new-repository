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
studentArray = []
#Student Array

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

 
  
with open('Dinner Seating - Student List 2018-19.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader: 
            if tables[line_count] == 'Kitchen Crew':
                kitchenCrew.append(Student(row[1], row[0], tables[line_count]))
            else:
                studentArray.append(Student(row[1],row[0],tables[line_count]))
            line_count += 1
print(studentArray)
print(kitchenCrew)
#Assigns each student Last Name, First Name to a table from randomized table array. Separates into tables in kitchen crew. 
