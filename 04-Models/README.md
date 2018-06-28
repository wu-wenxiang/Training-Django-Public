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