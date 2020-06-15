from django.contrib import admin
from shop import models 

# Register your models here.

class DepartementAdmin(admin.ModelAdmin):
	list_display = (
		'titre',
		'status',
		'date_cre',
		'date_mod',
	)
	list_filter = (
		'titre',
		'status',
	)
	search_fields = (
		'titre',
	)
	list_per_page = 10
	fieldsets = [
		('Info', {
			'fields':[
				'titre',
			]
		}),
		('Status et Activation', {
			'fields':[
				'status',
			]
		})
	]



class CategoryAdmin(admin.ModelAdmin):
	list_display = (
		'titre',
		'status',
		'departement',
		'date_cre',
		'date_mod',
	)
	list_filter = (
		'titre',
	)
	search_fields = (
		'titre',
	)
	list_per_page = 10
	fieldsets = [
		('Info', {
			'fields':[
				'titre',
				'departement',
			]
		}),
		('Status et Activation', {
			'fields':[
				'status',
			]
		})
	]

class ProductAdmin(admin.ModelAdmin):
	list_display = (
		'titre',
		'prix',
		'reduction',
		'image',
		'categorie',
		'status',
		'recommande',
	)
	list_filter = (
		'categorie',
	)
	search_fields = (
		'titre',
	)
	list_per_page = 10
	fieldsets = [
		('Info', {
			'fields':[
				'titre',
				'prix',
				'reduction',
				'image',
				'categorie',
				'description',


			]
		}),

		('Status et Activation', {
			'fields':[
				'recommande',
				'status',
			]
		})
	]

def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Product, ProductAdmin)

# enregistrement model departement
_register(models.Departement, DepartementAdmin)
#_register(models.Article, ArticleAdmin)

