from django.contrib import admin
from shop import models 

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = (
		'titre',
		'status',
		'date_cre',
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
		'categorie',
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
			]
		}),

		('Status et Activation', {
			'fields':[
				'status',
			]
		})
	]

def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Product, ProductAdmin)
#_register(models.Article, ArticleAdmin)

