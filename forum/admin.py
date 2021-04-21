from django.contrib import admin
from .models import ForumGroup, Forum, Topic, Post

admin.site.register(ForumGroup)
admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(Post)
