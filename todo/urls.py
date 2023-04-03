from django.urls import path

from todo.views import (
    TaskListView,
    TaskUpdateView,
    TaskCreateView,

    TagListView,
    TagUpdateView,
    TagCreateView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/create", TaskCreateView.as_view(), name="task-create"),

    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/create", TagCreateView.as_view(), name="tag-create"),
]

app_name = "todo"
