import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import csv
import random
from dataclasses import dataclass

@dataclass
class Student:
    firstName: str
    lastName: str

studentDict = {}

for i in range(0,32):
    if i == 0:
        studentDict['kitchen crew'] = dict()      
    else:
        studentDict['table'+str(i)] = dict()

with open('Dinner Seating - Student List 2018-19.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    current_table = 0
    person_number = 1
    waiter = False
    for row in csv_reader:
        if person_number == 9:
            waiter = True
        else:
            waiter = False
        if current_table == 0:
            studentDict['kitchen crew'].update({row[1] +' '+ row[0]: 'kitchen crew'})        
        else:
            if waiter == True:
                studentDict['table'+str(current_table)].update({row[1] +' '+ row[0]: 'table'+str(current_table)+'w'})
            else:
                studentDict['table'+str(current_table)].update({row[1] +' '+ row[0]: 'table'+str(current_table)})
        if current_table < 31:
            current_table += 1
        else:
            current_table = 0
            person_number += 1
print(studentDict)

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        requestPath = self.path
        #Log to us
        print(f'\n----- GET Request Start ----->\n')
        print(f'Request path: {requestPath}')
        print(f'Request headers:\n')
        for line in self.headers:
            print(f'  > {line}: {self.headers[line]}')
        print(f'\n<----- GET Request End -----\n')
        #Answer 200 => OK Status
        self.send_response(200)
        #Add Headers if any needed
        #self.send_header("Set-Cookie", "cate=true")
        self.end_headers()
        #Body of reply
        json_reply = json.dumps(studentDict)
        self.wfile.write(json_reply.encode(encoding='utf_8'))
# Listen on Port 80
port = 80
print('Listening on localhost:%s' % port)
server = HTTPServer(('', port), RequestHandler)
server.serve_forever()