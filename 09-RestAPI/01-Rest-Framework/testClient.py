import requests
url = 'http://localhost:8000/api/questions'
response = requests.get(url)
print(response.json())
print(response.text)
print(response.status_code)
# data ={
#     "id": 2,
#     "question_text": "What's new2?",
#     "pub_date": "2018-06-29T06:30:35+08:00"
# }
# response = requests.post(url, data=data)
# print(response.text)
# print(response.status_code)