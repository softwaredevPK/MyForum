from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import ListView
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import ForumGroup, Topic, Forum, Post
from .forms import PostForm

POSTS_PER_PAGE = 5


class ForumListView(ListView):
    model = ForumGroup
    template_name = 'forum/home.html'
    context_object_name = 'forum_groups'


class ForumTopicListView(ListView):
    model = Topic
    template_name = 'forum/topics.html'
    context_object_name = 'topics'

    def get_queryset(self):
        topics = Topic.objects.filter(forum_id=self.kwargs['forum_id']).order_by('date_posted')
        return topics


def posts(request, forum_pk, topic_pk):
    """Generates posts.html, which contains all posts related to certain topic in certain forum"""
    def get_posts(topic):
        my_objects = topic.post_set.all()
        return my_objects

    topic = get_object_or_404(Topic, pk=topic_pk, forum_id=forum_pk)
    query_set = get_posts(topic)
    paginator = Paginator(query_set, POSTS_PER_PAGE)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(POSTS_PER_PAGE)

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
        # each request for posts means viewing by someone
        topic.views += 1
        topic.save()

    return render(request, 'forum/posts.html', {'form': form, 'posts': posts, 'topic': topic, 'curr_page': page})
# todo missing token in html + check if user.authenticated
