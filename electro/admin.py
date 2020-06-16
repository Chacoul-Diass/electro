from django.contrib import admin
from electro import models 

# Register your models here.


class InfoAdmin(admin.ModelAdmin):
	list_display = (
		'telephone',
		'telephone2',
		'email',
		'address',
		'date_cre',
		'date_mod',
	)

	fieldsets = [
		('Info', {
			'fields':[
				'telephone',
				'telephone2',
				'email',
				'address',
					]
		}),
	]


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Info, InfoAdmin)