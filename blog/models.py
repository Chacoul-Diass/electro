from django.db import models


# Create your models here.

class BlogCategory(models.Model):
    titre = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'BlogCategory'
        verbose_name_plural = 'BlogCategories'

    def __str__(self):
        return str(self.titre)


class Auteur(models.Model):
    nom = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='blog/authors/photo', null=True, blank=True)
    description = models.TextField(null=True)

    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Auteur'
        verbose_name_plural = 'Auteurs'

    def __str__(self):
        return str(self.nom)


class Commentaire(models.Model):
    body = models.TextField()
    auteur = models.ForeignKey('Auteur', on_delete=models.CASCADE, related_name='commentaire_auteur')
    date_pub = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='commentaire_article')
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        return str(self.body)


class Article(models.Model):

    titre = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    body = models.TextField()
    categories = models.ManyToManyField('BlogCategory', related_name='categorieArticle')
    auteur = models.ForeignKey('Auteur', on_delete=models.CASCADE, related_name='article_auteur')
    date_pub = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog/articles/images', null=True, blank=True)

    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return str(self.titre)
