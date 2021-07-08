## 安装Django

- [选择合适的Python版本](https://www.djangoproject.com/download/)
- pip安装Django
	- `pip install django==1.11.21`
	- `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django==1.11.21`
	- `sudo pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django==1.11.21`
- pip卸载Django
	- `pip uninstall django`
	- `sudo pip uninstall django`
- 检查Django是否安装完成，以及Python版本
	- `python -m django --version`

## Hello, world

- 创建Django项目

	```bash
	# Windows
	python C:\Users\wenw\AppData\Local\Programs\Python\Python36\Scripts\django-admin.py startproject mysite
	# Linux/Mac
	django-admin.py startproject mysite
	```

- 上述命令会创建一个目录，结构如下：

	```console	
	# Windows
	> tree mysite /F
	C:\USERS\WENW\DESKTOP\TEST\MYSITE
	│  manage.py
	│
	└─ mysite
		    settings.py
		    urls.py
	        wsgi.py
	        __init__.py
	
	# Linux
	$ find mysite
	mysite
	mysite/mysite
	mysite/mysite/__init__.py
	mysite/mysite/settings.py
	mysite/mysite/urls.py
	mysite/mysite/wsgi.py
	mysite/manage.py
	```

- 把这个项目跑起来

	```bash
	cd mysite
	# 在localhost:8000端口跑起来
	python manage.py runserver
	# 在0.0.0.0:8000端口跑起来
	# python manage.py runserver 0:8000
	# python manage.py runserver 0.0.0.0:8000
	```

- 现在可以在浏览器上访问：`http://localhost:8000/`，可以看到蓝色的django欢迎界面。

	![Django-Welcome.png](/images/a419720ca0ad4c2582a5b5ee48e53b02-Django-Welcome.png)

- 修改urls.py，添加第一个视图函数hello，[源码](01-Hello-World)

	```console
	$ git diff mysite/urls.py 
	 """
	 from django.conf.urls import url
	 from django.contrib import admin
	+from django.http.response import HttpResponse
 	+
	+def hello(request):
	+    return HttpResponse('Hello World')
		 
	 urlpatterns = [
	+    url(r'^hello/', hello),
		 url(r'^admin/', admin.site.urls),
	 ]
	```

- 访问到错误的URL时，可以看到404页面，带url列表信息

	![Django-URL-404.png](/images/a419720ca0ad4c2582a5b5ee48e53b02-Django-URL-404.png)

- 访问到争取的页面时，可以看到hello, world

	![Django-HelloWorld.png](/images/a419720ca0ad4c2582a5b5ee48e53b02-Django-HelloWorld.png)

- Console中可以看到访问记录

	![Django-Console.png](/images/a419720ca0ad4c2582a5b5ee48e53b02-Django-Console.png)

- Browser中可以看到HTTP请求过程

## Project, App & First View

- 创建app
	- `python manage.py startapp polls`
- 上述命令会创建一个目录polls，与manage.py在同级目录下

	```console	
	$ tree
	.
	├── manage.py
	├── mysite
	│   ├── __init__.py
	│   ├── __pycache__
	│   │   ├── __init__.cpython-36.pyc
	│   │   └── settings.cpython-36.pyc
	│   ├── settings.py
	│   ├── urls.py
	│   └── wsgi.py
	└── polls
		├── __init__.py
	    ├── admin.py
	    ├── apps.py
		├── migrations
	    │   └── __init__.py
	    ├── models.py
		├── tests.py
	    └── views.py	    
	```

- 将helloworld中的hello方法移动到views.py中，[源码](02-First-View)
