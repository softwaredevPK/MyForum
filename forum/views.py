from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import ListView
from django.http import Http404
from .forms import PostForm


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


def posts(request, forum_pk, topic_pk):
    def get_posts(topic):
        my_objects = topic.post_set.all()
        return my_objects

    topic = get_object_or_404(Topic, pk=topic_pk, forum_id=forum_pk)
    query_set = get_posts(topic)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            topic = get_object_or_404(Topic, pk=request.resolver_match.kwargs['topic_pk'])
            form.instance.topic = topic
            post_item = form.save(commit=False)
            if post_item.content.strip() != '':
                post_item.save()
                return redirect(request.path_info)
    else:
        form = PostForm

    return render(request, 'forum/posts.html', {'form': form, 'posts': query_set, 'topic': topic})
# todo missing token in html + check if user.authenticated
