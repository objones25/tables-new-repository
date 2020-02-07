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

for student in studentArray:
    #print(student)
    randomInt = random.randint(0,31)
    full_table = False
    while full_table == False:
        if len(tableArray[randomInt]) >= 9 and randomInt >= 2:
            if randomInt <= 30:
                randomInt += 1
            else:
                randomInt = 0 
        #if any other table is full, check next table
        elif len(tableArray[randomInt]) >= 10:
            if randomInt <= 30:
                randomInt += 1
            else:
                randomInt = 0 
        #if table 0 or 1 is full, check next table   
        else:
            #print(randomInt)
            full_table = True
        #once table is determined to have space check no more tables
    tableArray[randomInt].append(student)
    #picks random table, if table is full, choose new table. Kitchen crew and Table 1 have 10 people rest have 9 
    
    randomInttwo = random.randint(0,31)
    full_table = False
    tables_checked = 0
    while full_table == False:
        if tables_checked >= 32:
            student_swap = random.randint(0,31)
            while student_swap == randomInt:
                student_swap += 1
            tableArrayTwo[randomInttwo].append(tableArrayTwo[student_swap][0])
            tableArrayTwo[randomInttwo].remove(tableArrayTwo[randomInttwo][0])
        #If all tables have been checked swap with the first student at a random table
        if len(tableArrayTwo[randomInttwo]) >= 9 and randomInttwo >= 2:
            if randomInttwo <= 30:
                randomInttwo += 1
                tables_checked += 1
            else:
                randomInttwo = 0
                tables_checked +=1
        #if any other table is full, check next table  
        elif len(tableArrayTwo[randomInttwo]) >= 10:
            if randomInttwo <= 30:
                randomInttwo += 1
                tables_checked += 1
            else:
                randomInttwo = 0 
                tables_checked +=1
        #if table 0 or 1 is full, check next table 
        elif randomInttwo == randomInt:
            if randomInttwo <= 30:
                randomInttwo += 1
                tables_checked += 1
            else:
                randomInttwo = 0
                tables_checked += 1
        #if student has already sat at table, check next table
        else:
            #print(randomInttwo)
            full_table = True
        #once table is determined to have space check no more tables
    tableArrayTwo[randomInttwo].append(student) 
    #picks random table. if student has already sat at table or table is full, choose new table. If no table is available that student hasn't sat at, swaps with random student

    randomIntthree = random.randint(0,31)
    full_table = False
    tables_checked = 0
    while full_table == False:
        if tables_checked >= 32:
            student_swap = random.randint(0,31)
            while student_swap == randomInt or student_swap == randomInttwo:
                student_swap += 1
            tableArrayThree[randomIntthree].append(tableArrayThree[student_swap][0])
            tableArrayThree[randomIntthree].remove(tableArrayThree[randomIntthree][0])
            #If all tables have been checked swap with the first student at a random table
        if (len(tableArrayThree[randomIntthree]) >= 9 and randomIntthree >= 2):
            if randomIntthree <= 30:
                randomIntthree += 1
                tables_checked += 1
            else:
                randomIntthree = 0
                tables_checked +=1  
        #if any other table is full, check next table     
        elif (len(tableArrayThree[randomIntthree]) >= 10):
            if randomIntthree <= 30:
                randomIntthree += 1
                tables_checked += 1
            else:
                randomIntthree = 0
                tables_checked += 1 
        #if table 0 or 1 is full, check next table  
        elif randomIntthree == randomInt or randomIntthree == randomInttwo:
            if randomIntthree <= 30:
                randomIntthree += 1
                tables_checked += 1
            else:
                randomIntthree = 0
                tables_checked += 1
        #if student has already sat at table, check next table
        else:
            #print(randomIntthree)
            full_table = True
        #once table is determined to have space check no more tables
    tableArrayThree[randomIntthree].append(student)
    #picks random table. if student has already sat at table or table is full, choose new table. If no table is available that student hasn't sat at, swaps with random student

print('first seating')
for x in range(0,32):
    if x == 0:
        print('kitchen crew')
    else:
        print('table' + str(x))
    print(tableArray[x])
    #print(len(tableArray[x]))
    print('waiter')
    print(tableArray[x][random.randint(0,8)])
    #prints table assignments. Assigns random waiter

print('second seating')
for x in range(0,32):
    if x == 0:
        print('kitchen crew')
    else:
        print('table' + str(x))
    print(tableArrayTwo[x])
    #print(len(tableArrayTwo[x]))
    print('waiter')
    print(tableArrayTwo[x][random.randint(0,8)])
    #prints table assignments. Assigns random waiter

print('third seating')
for x in range(0,32):
    if x == 0:
        print('kitchen crew')
    else:
        print('table' + str(x))
    print(tableArrayThree[x])
    #print(len(tableArrayThree[x]))
    print('waiter')
    print(tableArrayThree[x][random.randint(0,8)])
    #prints table assignments. Assigns random waiter
    