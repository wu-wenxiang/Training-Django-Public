import requests
url = 'http://localhost:8000/api/questions'
url = url.rstrip('/')+'/'
 
response = requests.get(url)
print(response.json())
print(response.text)
print(response.status_code)

import random
i = random.randint(10000, 20000)
data ={
    "id": i,
    "question_text": "What's new{}?".format(i),
    "pub_date": "2018-06-29T06:30:35+08:00"
}
response = requests.post(url, data=data)
print(response.text)
print(response.status_code)
print(response.json())