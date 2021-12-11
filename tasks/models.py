from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import SET_NULL

class Categoria(models.Model):
	categoria = models.CharField(max_length=50)
	icone = models.CharField(max_length=20)

	def __str__(self):
		return self.categoria

class Task(models.Model):
	
	STATUS = (
		('doing', 'Doing'),
		('done', 'Done'),
	)

	title = models.CharField('Título', max_length=255)
	description = models.TextField('Descrição', blank=True)
	categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True, blank=True)
	data = models.DateTimeField(blank=True, null=True)
	done = models.CharField(max_length=5,
		choices=STATUS,
	)
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title