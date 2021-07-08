## 创建Admin账户

- 运行命令，创建Admin账户，密码要满足复杂度要求

        $ python manage.py createsuperuser
        Username (leave blank to use 'wxdev_mac'): admin
        Email address: admin@example.com
        Password: 123(3*)#xyz
        Password (again): 123(3*)#xyz 
        Superuser created successfully.

- 然后可以登陆Admin Portal
    - 把Debug WebServer跑起来：`python manage.py runserver`
    - 登陆试试：http://localhost:8000/admin/
    
        ![Admin Login](https://docs.djangoproject.com/en/1.11/_images/admin01.png)

        ![Admin Portal](https://docs.djangoproject.com/en/1.11/_images/admin02.png) 

## 将App注册到Admin界面

- 修改 [admin.py](01-Register-App/mysite/polls/admin.py)

    ```python
    from django.contrib import admin
    from .models import Question
    admin.site.register(Question)
    ```

    ![Admin polls](https://docs.djangoproject.com/en/1.11/_images/admin03t.png)

- 现在我们可以在Admin中修改Question数据表中的每一项

    ![Admin Question](https://docs.djangoproject.com/en/1.11/_images/admin04t.png)

    ![Admin Edit](https://docs.djangoproject.com/en/1.11/_images/admin05t.png)

- 修改完成后，所有历史修改记录会被保留

    ![Admin History](https://docs.djangoproject.com/en/1.11/_images/admin06t.png)
