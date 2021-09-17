from django.db import models

# Create your models here.
class Expense(models.Model):
	title = models.CharField(max_length=100)
	amount = models.TextField()
	date = models.DateField()

	def __str__(self):
		return self.title
	"""
	id: 'e1',
            title: 'Oreo',
            amount: 940.12,
            date: new Date(2020, 7, 14),
   """