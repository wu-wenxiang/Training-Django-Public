## Migration
- 在配置文件`mysite.settings`中，可以看到DB的配置

		# Database
		# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
		
		DATABASES = {
		    'default': {
		        'ENGINE': 'django.db.backends.sqlite3',
		        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		    }
		}
- 默认启用的App

		# Application definition

		INSTALLED_APPS = [
		    'django.contrib.admin',        # 后台管理
		    'django.contrib.auth',         # 验证系统
		    'django.contrib.contenttypes', # 内容类型框架
		    'django.contrib.sessions',     # Session
		    'django.contrib.messages',     # Message 
		    'django.contrib.staticfiles',  # 静态文件
		]
- 上述默认启用的App有些会需要用到DB，比如Admin，因此需要产生对应的DB Table。
	- 使用命令：`python manage.py migrate`
	- 这个命令会遍历INSTALLED_APPS中所有App的模型对象，建立必要的Table
	- 建立Table时，对不同的数据库类型，会对应地产生不同的SQL语句
- 命令执行输出：	

		$ python manage.py migrate
		Operations to perform:
		  Apply all migrations: admin, auth, contenttypes, sessions
		Running migrations:
		  Applying contenttypes.0001_initial... OK
		  Applying auth.0001_initial... OK
		  Applying admin.0001_initial... OK
		  Applying admin.0002_logentry_remove_auto_add... OK
		  Applying contenttypes.0002_remove_content_type_name... OK
		  Applying auth.0002_alter_permission_name_max_length... OK
		  Applying auth.0003_alter_user_email_max_length... OK
		  Applying auth.0004_alter_user_username_opts... OK
		  Applying auth.0005_alter_user_last_login_null... OK
		  Applying auth.0006_require_contenttypes_0002... OK
		  Applying auth.0007_alter_validators_add_error_messages... OK
		  Applying auth.0008_alter_user_username_max_length... OK
		  Applying sessions.0001_initial... OK

## Add Model
- [Add model](https://github.com/wu-wenxiang/Training-Django-Public/blob/master/04-Models/02-Add-Model/mysite/polls/models.py)
	
		# Create your models here.
		from django.db import models
		
		class Question(models.Model):
		    question_text = models.CharField(max_length=200)
		    pub_date = models.DateTimeField('date published')
		
		class Choice(models.Model):
		    question = models.ForeignKey(Question, on_delete=models.CASCADE)
		    choice_text = models.CharField(max_length=200)
		    votes = models.IntegerField(default=0)
- [on_delete](https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.ForeignKey.on_delete)
	- **CASCADE**: When the referenced object is deleted, also delete the objects that have references to it (When you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.
	- **PROTECT**: Forbid the deletion of the referenced object. To delete it you will have to delete all objects that reference it manually. SQL equivalent: RESTRICT.
	- **SET_NULL**: Set the reference to NULL (requires the field to be nullable). For instance, when you delete a User, you might want to keep the comments he posted on blog posts, but say it was posted by an anonymous (or deleted) user. SQL equivalent: SET NULL.
	- **SET_DEFAULT**: Set the default value. SQL equivalent: SET DEFAULT.
	- **SET(...)**: Set a given value. This one is not part of the SQL standard and is entirely handled by Django.
	- **DO_NOTHING**: Probably a very bad idea since this would create integrity issues in your database (referencing an object that actually doesn't exist). SQL equivalent: NO ACTION.
- 添加`polls`子站点到`INSTALLED_APPS`

		INSTALLED_APPS = [
		    'polls.apps.PollsConfig',
		    'django.contrib.admin',
		    ...
		]
- makemigrations，创建一个Migration版本：该版本会创建表Choice和Question
	
		$ python manage.py makemigrations polls
		Migrations for 'polls':
		  polls/migrations/0001_initial.py
		    - Create model Choice
		    - Create model Question
		    - Add field question to choice
- sqlmigrate命令可以查看makemigrations对应的SQL语句
	- `python manage.py sqlmigrate polls 0001`
- 最后运行migrate命令，令各个Migration版本生效

		$ python manage.py migrate
		Operations to perform:
		  Apply all migrations: admin, auth, contenttypes, polls, sessions
		Running migrations:
		  Applying polls.0001_initial... OK

## 总结为App添加模型的过程
1. Change your models (in models.py).
1. 如果没有将App注册到INSTALLED_APPS，那就注册一下
1. 运行`python manage.py makemigrations <app>`，创建一个migration版本
1. 运行`python manage.py sqlmigrate <app> <version>`，查看该migration版本变更对应的SQL语句是什么。
1. 运行`python manage.py migrate`，将各个migrations应用到DB