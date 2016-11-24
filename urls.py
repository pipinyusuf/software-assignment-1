from django.conf.urls import url

from .views import show_todo, get_todo

urlpatterns = [
    url(r'^blog/entries/$', show_todo),
    url(r'^blog/entries(?P<todo_id>[0-9]+)', get_todo)
]
