from django.db import models

# Create your models here.

class Departement(models.Model):
	titre = models.CharField(max_length=255)
	status = models.BooleanField(default=True)

	date_cre = models.DateTimeField(auto_now_add=True)
	date_mod = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Departement"
		verbose_name_plural = "Departements"

	def __str__(self):
		return self.titre



class Category(models.Model):
	titre = models.CharField(max_length=255)
	status = models.BooleanField(default=True)
	departement = models.ForeignKey('Departement', on_delete=models.CASCADE, related_name = 'departement')

	date_cre = models.DateTimeField(auto_now_add=True)
	date_mod = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Categorie"
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.titre


class Product(models.Model):
	titre = models.CharField(max_length=255)
	detais = models.CharField(max_length=255)
	image = models.ImageField(upload_to = 'shop/produit/image', blank=True, null =True)
	prix = models.FloatField()
	reduction = models.FloatField(blank=True)
	categorie = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'categorie')
	status = models.BooleanField(default=True)


	date_cre = models.DateTimeField(auto_now_add=True)
	date_mod = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "product"
		verbose_name_plural = "Products"

	def __str__(self):
		return self.titre


