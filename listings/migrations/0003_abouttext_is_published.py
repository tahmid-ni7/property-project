# Generated by Django 2.2.5 on 2020-02-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20200207_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='abouttext',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]