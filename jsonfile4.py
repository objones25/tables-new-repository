import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import csv



with open('Dinner Seating - Student List 2018-19.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    current_table = 0
    person_number = 1
    waiter = False
    studentDict = {}
    for row in csv_reader:
        studentDict[str(row[1] +' '+ row[0])] = dict()
        if person_number == 9:
            waiter = True
        else:
            waiter = False
        if current_table == 0:
            studentDict[str(row[1] +' '+ row[0])].update({'firstName': row[1], 'lastName': row[0], 'seating': 'kitchen crew', 'isWaiter': 'no' })        
        else:
            if waiter == True:
                studentDict[str(row[1] +' '+ row[0])].update({'firstName': row[1], 'lastName': row[0], 'seating': str(current_table), 'isWaiter': 'yes'})
            else:
                studentDict[str(row[1] +' '+ row[0])].update({'firstName': row[1], 'lastName': row[0], 'seating': str(current_table), 'isWaiter': 'no'})
        if current_table < 31:
            current_table += 1
        else:
            current_table = 0
            person_number += 1
print(studentDict)
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        requestPath = self.path
        
        if '%20'in requestPath:
            print('I got this far')
            key = '%20'
            print(key)
            newUrl = requestPath.replace(key, '+')
            print(newUrl)
            keyword = newUrl.replace('+', ' ')
            print (keyword)

        if '/'in requestPath:   
            print('next key variable') 
            key = '/' 
            title = keyword.replace(key, '+')
            print(title)
            name = title.replace('+', '')
            print(name)
            # title_text_data_file = title_text_data_file + ".txt"
            requestPath = name 
            print(requestPath)
            print('done with this function')

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

        #Look up your requested student (requestPath) in studentDict

        #Look up other students at that table

        #Put a string together that has the json reply
        placement = studentDict[requestPath]['seating']
        waiter = studentDict[requestPath]['isWaiter']
        print(placement)
        SeatingData = json.dumps({'name': requestPath,'seating': placement, 'isWaiter': waiter})
        print(SeatingData)
        self.wfile.write(SeatingData.encode(encoding='utf_8'))
        for student in studentDict:
            if studentDict[student]['seating'] == placement
            
# Listen on Port 80
port = 80
print('Listening on localhost:%s' % port)
server = HTTPServer(('', port), RequestHandler)
print(server)
server.serve_forever()