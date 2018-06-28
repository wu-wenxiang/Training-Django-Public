## 更多Urls, Views和Templates
- 为Views添加更多函数
    - `/polls/`
    - `/polls/5/`
    - `/polls/5/results/`
    - `/polls/5/vote/`
- Add Choice

        $ python manage.py shell

        >>> django.setup()
        >>> import django
        >>> django.setup()
        
        >>> from polls.models import Question, Choice 
        >>> from django.utils import timezone
        
        >>> Question.objects.all()
        <QuerySet [<Question: What's new?>]>
        >>> q = Question.objects.get(id=1)
        >>> q.choice_set.all()
        <QuerySet []>
        
        >>> q.choice_set.create(choice_text='Not much', votes=0)
        <Choice: Not much>
        >>> q.choice_set.create(choice_text='The sky', votes=0)
        <Choice: The sky>
        >>> q.choice_set.create(choice_text='Just hacking again', votes=0)
        <Choice: Just hacking again>
        >>> q.choice_set.all()
        <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
        >>> q.save()

## Add Form

    