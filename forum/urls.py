"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import ForumListView, ForumTopicListView,  posts
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', ForumListView.as_view(), name='main-page'),
    path('forum/<int:forum_id>/', ForumTopicListView.as_view(), name='topics-page'),
    path('forum/<int:forum_pk>/<int:topic_pk>', posts, name='posts-page')]\
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
