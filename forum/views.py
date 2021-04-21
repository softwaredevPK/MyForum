from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView


from .models import ForumGroup, Topic, Forum


class ForumListView(ListView):
    model = ForumGroup
    template_name = 'forum/home.html'
    context_object_name = 'forum_groups'


class ForumTopicListView(ListView):
    model = Topic
    template_name = 'forum/topics.html'
    context_object_name = 'forum'

    def get_queryset(self):
        forum = get_object_or_404(Forum, pk=self.kwargs['pk'])
        return forum
