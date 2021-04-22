from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView
from django.http import Http404


from .models import ForumGroup, Topic, Forum, Post


class ForumListView(ListView):
    model = ForumGroup
    template_name = 'forum/home.html'
    context_object_name = 'forum_groups'


# todo template for below view need an upgrade
class ForumTopicListView(ListView):
    model = Topic
    template_name = 'forum/topics.html'
    context_object_name = 'forum'

    def get_queryset(self):
        forum = get_object_or_404(Forum, pk=self.kwargs['pk'])
        return forum


# todo for below View template not prepared
class TopicPostListView(ListView):
    model = Post
    template_name = 'forum/posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 8

    def get_queryset(self):
        topic = get_object_or_404(Topic, pk=self.kwargs['topic_pk'], forum_id=self.kwargs['topic_pk'])
        my_objects = topic.post_set.all()
        if not my_objects:
            raise Http404("No MyModel matches the given query.")
        return my_objects

