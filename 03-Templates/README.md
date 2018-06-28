## Django Shell

	$ ls
	manage.py  mysite     polls      templates
	  
	$ python
	>>> import os
	>>> os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
	'mysite.settings'
	>>> import django
	>>> django.setup()
	>>> from django import template
	>>> t = template.Template('My name is {{ name }}.')
	>>> c = template.Context({'name': 'Adrian'})
	>>> print(t.render(c))
	My name is Adrian.

## Steps
1. [Add-Template](https://github.com/wu-wenxiang/Training-Django-Public/tree/master/03-Templates/01-Add-Template)
1. [Template-Base](https://github.com/wu-wenxiang/Training-Django-Public/tree/master/03-Templates/02-Template-Base)