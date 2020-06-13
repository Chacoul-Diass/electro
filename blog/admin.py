from django.contrib import admin
from blog import models


# Register your models here.


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'status',

    )
    list_filter = (
        'status',
    )
    search_fields = (
        'titre',
    )
    list_per_page = 10
    fieldsets = [
        ('Info', {
            'fields': [
                'titre',
            ]
        }),
        ('Status et Activation', {
            'fields': [
                'status',
            ]
        })
    ]


class AuteurAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'description',
        'status',

    )
    list_filter = (
        'status',
    )
    search_fields = (
        'nom',
    )
    list_per_page = 10
    fieldsets = [
        ('Info', {
            'fields': [
                'nom',
                'description',
            ]
        }),
        ('Status et Activation', {
            'fields': [
                'status',
            ]
        })
    ]


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'auteur',
        'date_pub',
        'date_mod',
    )
    list_filter = (
        'status',
        'auteur',
        'date_pub',
        'date_mod',
        'categories',
    )
    search_fields = (
        'titre',
    )
    list_per_page = 10
    fieldsets = [
        ('Informations Article', {
            'fields': [
                'titre',
                'description',
                'categories',
                'auteur',
            ]
        }),
        ('Image', {
            'fields': [
                'image',
            ]
        }),
        ('Status et Activation', {
            'fields': [
                'status',
            ]
        })
    ]


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.BlogCategory, BlogCategoryAdmin)
_register(models.Auteur, AuteurAdmin)
_register(models.Article, ArticleAdmin)
