# Generated by Django 5.1 on 2024-11-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0017_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
