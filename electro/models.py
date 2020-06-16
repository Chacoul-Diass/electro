from django.db import models

# Create your models here.

class Info(models.Model):
	telephone = models.CharField(default='99999999', max_length=8)
	telephone2 = models.CharField(default='99999999', max_length=8)

	email = models.CharField(default='electro@email.com', max_length=50)

	address = models.CharField(max_length=255, default='17 Princess Road, London, Greater London NW1 8JR, UK')

	date_cre = models.DateTimeField(auto_now_add=True)
	date_mod = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Info"
		verbose_name_plural = "Infos"

	def __str__(self):
		return self.address
