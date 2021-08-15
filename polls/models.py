from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'  # pub_date로 정렬하겠다
    was_published_recently.boolean = True  # 아이콘 모양으로 바꿔줌
    was_published_recently.short_description = "Published recently?"  # 타이틀 변경


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Acount_Login(models.Model):
    IDwlgns = models.CharField(max_length= 20, primary_key=True, unique=True)
    passwordwlgns = models.CharField(max_length= 20)

    def __str__(self):
        return self.userid


