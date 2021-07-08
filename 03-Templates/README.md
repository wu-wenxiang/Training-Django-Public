## Django Shell

	$ ls
	manage.py  mysite     polls      templates
	
	$ python manage.py shell
	>>> import django
	>>> django.setup()
	>>> from django import template
	>>> t = template.Template('My name is {{ name }}.')
	>>> c = template.Context({'name': 'Adrian'})
	>>> print(t.render(c))
	My name is Adrian.
	
	# 如果直接进入python交互环境
	# 必须制定 DJANGO_SETTINGS_MODULE 环境变量
	# 其它和从python manage.py shell进入没有区别
	$ python
	>>> import os
	>>> os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
	'mysite.settings'
	>>> import django
	>>> django.setup()


## Steps

1. [Add-Template](01-Add-Template)
1. [Template-Base](02-Template-Base)