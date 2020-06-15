# Generated by Django 2.2.13 on 2020-06-14 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaire_article', to='blog.Article')),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaire_auteur', to='blog.Auteur')),
            ],
            options={
                'verbose_name': 'Commentaire',
                'verbose_name_plural': 'Commentaires',
            },
        ),
    ]