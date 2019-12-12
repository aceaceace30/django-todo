from django.db import models
from django.contrib.auth.models import AbstractUser

from django.urls import reverse

class User(AbstractUser):
	pass


class Todo(models.Model):

	title = models.CharField(max_length=100)
	description = models.TextField(max_length=500)
	completed = models.BooleanField(default=False)

	created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_create')
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_update')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('mytodo:todo_detail', kwargs={'pk': self.pk})