import requests 
import json
import csv
import re

a = [["name","age",'count']] #array for csv.writer() with header
names = [] #list of possible names for requests
pattern = r"[A-Z]" #filter for non-latin letters
qty = int(input("How many names do you want to extract?"))
b = qty

while b != 0:   #collecting random names from https://randomuser.me/api/
    r = requests.get('https://randomuser.me/api/') 
    j = json.loads(r.text)
    if re.match(pattern,j['results'][0]['name']['first']):
        names.append(j['results'][0]['name']['first'])
        b -= 1

for name in names:      #collecting API responces to every name
    r = requests.get(f'https://api.agify.io/?name={name}')  #required API request
    j = json.loads(r.text)
    d = []
    for i in j.values():       
        d.append(i)
    a.append(d)             #updating array "a" with header

with open("result.csv",'w',newline='',encoding='utf-8') as f: #create and write data from requests/array "a"
    writer = csv.writer(f)
    writer.writerows(a)
print(f"Extracting finished. CSV file with {qty} names is created.")


