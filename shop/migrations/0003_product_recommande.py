# Generated by Django 2.2.13 on 2020-06-15 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200613_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='recommande',
            field=models.BooleanField(default=False),
        ),
    ]