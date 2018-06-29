## Add Unit Test
- add test case in test.py
- 运行命令：`python manage.py test pools`

        $ python manage.py test polls
        Creating test database for alias 'default'...
        System check identified no issues (0 silenced).
        F
        ======================================================================
        FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
          File "mysite/polls/tests.py", line 21, in test_was_published_recently_with_future_question
            self.assertIs(future_question.was_published_recently(), False)
        AssertionError: True is not False
        
        ----------------------------------------------------------------------
        Ran 1 test in 0.001s
        
        FAILED (failures=1)
        Destroying test database for alias 'default'...
- 修改Bug

        #polls/models.py
        
        def was_published_recently(self):
            now = timezone.now()
            return now - datetime.timedelta(days=1) <= self.pub_date <= now