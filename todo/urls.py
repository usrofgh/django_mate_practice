from django.urls import path

from todo.views import TaskListView, TagListView, TagUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),

    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/", TagUpdateView.as_view(), name="tag-update")
]

app_name = "todo"
