from django.db import models

# Create your models here.
class Search(models.Model):
	search_field = models.CharField(max_length =200)
	date_created = models.DateTimeField(auto_now = True)
	
	class Meta:
		verbose_name_plural = 'Searches'
	def __str__(self):
		return self.search_field