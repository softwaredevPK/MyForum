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


def topic_posts(request, forum_pk, topic_pk):
    def get_posts():
        topic = get_object_or_404(Topic, pk=topic_pk, forum_id=forum_pk)
        my_objects = topic.post_set.all()
        if not my_objects:
            raise Http404("No MyModel matches the given query.")
        return my_objects

    query_set = get_posts()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('/')
    else:
        form = PostForm

    return render(request, 'forum/posts.html', {'form': form, 'posts': query_set})
# todo missing token in html + check if user.authenticated
