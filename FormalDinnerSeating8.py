import csv
import random
from dataclasses import dataclass

@dataclass
class Student:
    firstName: str
    lastName: str
   

studentArray = []
tableArray = [[] for i in range(0,32)]
tableArrayTwo = [[] for i in range(0,32)]
tableArrayThree = [[] for i in range(0,32)]
#creates array of 31 tables plus one kitchen crew

with open('Dinner Seating - Student List 2018-19.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader: 
        studentArray.append(Student(row[1],row[0]))

current_table = 0
for student in studentArray:
    tableArray[current_table].append(student)
    if current_table < 31:
        current_table += 1
    else:
        current_table = 0

for x in range(0,32):
    if x == 0:
        print('kitchen crew')
    else:
        print('table' + str(x))
    for i in range (0,len(tableArray[x])):
        if i == (len(tableArray[x])-1) and x > 0:
            print('waiter')
        print(tableArray[x][i])

for x in range(0,32):
    next_table = 0
    for student in tableArray[x]:
        next_table +=1
        if (x + next_table) > 31:
            next_table -= 32
        tableArrayTwo[(x+next_table)].append(student)

for x in range(0,32):
    if x == 0:
        print('kitchen crew')
    else:
        print('table' + str(x))
    for i in range (0,len(tableArrayTwo[x])):
        if i == (len(tableArrayTwo[x])-1) and x > 0:
            print('waiter')
        print(tableArrayTwo[x][i])


for x in range(0,32):
    next_table = 0
    for student in tableArrayTwo[x]:
        next_table +=1
        if (x + next_table) > 31:
            next_table -= 32
        tableArrayThree[(x+next_table)].append(student)

for x in range(0,32):
    if x == 0:
        print('kitchen crew')
    else:
        print('table' + str(x))
    for i in range (0,(len(tableArrayThree[x]))):
        if i == (len(tableArrayThree[x])-1) and x > 0:
            print('waiter')
        print(tableArrayThree[x][i])
    


