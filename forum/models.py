from django.db import models


class ForumGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Forum(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=350)
    group = models.ForeignKey(ForumGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.title