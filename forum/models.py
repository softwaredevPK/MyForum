from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField


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

    def posts_no(self):
        return self.topic_set.aggregate(models.Count('post'))['post__count'] + self.topic_set.count() + 1  # topics itself are considered as posts

    def last_topic(self):
        return self.topic_set.latest('date_posted')


class Topic(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    views = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now, auto_now_add=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # RODO
    forum = models.ForeignKey(Forum, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def responses(self):
        return self.post_set.count()

    def last_post(self):
        try:
            return self.post_set.latest('date_posted')
        except models.ObjectDoesNotExist:  # if there are no posts under topic, it means topic itself was last post
            return self

    def new_post_today(self):
        now = timezone.now()
        # topic is considered as post, so if one was created return True
        if self.date_posted.year == now.year and self.date_posted.month == now.month and self.date_posted.day == now.day:
            return True
        else:
            try:
                last_post = self.post_set.latest('date_posted')
            except models.ObjectDoesNotExist:  # if there are no posts and topic wasn't created now return False
                return False
            # post found so there is need to check latest one
            if last_post.date_posted.year == now.year and last_post.date_posted.month == now.month and last_post.date_posted.day == now.day:
                return True
            else:
                return False


class Post(models.Model):
    content = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # RODO
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # RODO
    date_posted = models.DateTimeField(default=timezone.now, auto_now_add=False)

    def __str__(self):
        return self.author.username + f' - {self.topic} - {self.date_posted.strftime("%a %H:%M  %d/%m/%y")}'
