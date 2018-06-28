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