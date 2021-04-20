from django.shortcuts import render
from django.views.generic import ListView


from .models import ForumGroup


class ForumListView(ListView):
    model = ForumGroup
    template_name = 'forum/home.html'
    context_object_name = 'forum_groups'
