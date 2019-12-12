from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from mytodo.models import Todo

class TodoCreateView(CreateView):

	model = Todo
	fields = ('title', 'description')

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		form.instance.updated_by = self.request.user
		return super().form_valid(form)

class TodoDetailView(DetailView):

	model = Todo
	context_object_name = 'todo'

class TodoUpdateView(UpdateView):

	model = Todo
	fields = ('title', 'description')

	def form_valid(self, form):
		form.instance.updated_by = self.request.user
		return super().form_valid(form)

class TodoListView(ListView):

	#login_url = settings.LOGIN_URL

	model = Todo
	context_object_name = 'todos'

class TodoDeleteView(DeleteView):

	model = Todo
	context_object_name = 'todo'
	success_url = reverse_lazy('mytodo:todo_list')
