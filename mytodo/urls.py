from django.urls import path
from mytodo.views.mytodo import *

app_name = 'mytodo'

urlpatterns = [
	path('todo_create/', TodoCreateView.as_view(), name='todo_create'),
	path('todo_detail/<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
	path('todo_update/<int:pk>/', TodoUpdateView.as_view(), name='todo_update'),
	path('todo_list/', TodoListView.as_view(), name='todo_list'),
	path('todo_delete/<int:pk>/', TodoDeleteView.as_view(), name='todo_delete'),
]