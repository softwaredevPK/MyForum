from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ForumGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Forum(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=350)
    group = models.ForeignKey(ForumGroup, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # RODO
    forum = models.ForeignKey(Forum, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # RODO
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # RODO
    date_posted = models.DateTimeField(default=timezone.now, auto_now_add=False)

    def __str__(self):
        return self.author.username + f' - {self.topic} - {self.date_posted.strftime("%a %H:%M  %d/%m/%y")}'
