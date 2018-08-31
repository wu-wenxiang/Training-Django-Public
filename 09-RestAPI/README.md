- [django-rest-framework quickstart](http://www.django-rest-framework.org/tutorial/quickstart/)
- [django-rest-framework reference](https://github.com/twtrubiks/django-rest-framework-tutorial)
- [Postman](https://www.getpostman.com/apps)
- curl

		curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/questions/
		[
		    {
		        "id": 1,
		        "question_text": "What's new?",
		        "pub_date": "2018-06-29T06:30:35+08:00"
		    }
		]
		
		curl -H 'Accept: application/json; indent=4' http://127.0.01:8000/api/users/
		[
		    {
		        "url": "http://127.0.0.1:8000/api/users/1/",
		        "username": "admin",
		        "email": "admin@example.com",
		        "groups": []
		    }
		]