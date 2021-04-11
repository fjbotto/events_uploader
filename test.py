import requests

BASE = "http://127.0.0.1:5000/"

data = [
   {"likes": 20, "name": "Testing python", "views": 45000},
   {"likes": 5670, "name": "Testing Flask", "views": 122000},
   {"likes": 100, "name": "Testing API Restful", "views": 100},
   {"likes": 1, "name": "Testing BLA BLA", "views": 10}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()

#response = requests.delete(BASE + "vide/0")
#print(response)

response = requests.get(BASE + "video/2")
print(response.json())

response = requests.get(BASE + "video/12")
print(response.json())

input()

response = requests.patch(BASE + "video/2", {"views": 199, "likes": 101, "name": "Fede"})
print(response.json())