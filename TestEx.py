import requests 
import json
import csv

a = [["name","age",'count']] #array for csv.writer() with header

names = ["Boris", "Ivan", "Smith", "Bob","Bruce"] #possible names for requests
for name in names:
    r = requests.get(f'https://api.agify.io/?name={name}')  #API request
    j = json.loads(r.text)
    d = []
    for i in j.values():       #updating array "a"
        d.append(i)
    a.append(d)    
with open("result.csv",'w',newline='') as f: #create and write data from requests/array "a"
    writer = csv.writer(f)
    writer.writerows(a)