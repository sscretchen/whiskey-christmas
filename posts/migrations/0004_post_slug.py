# Generated by Django 3.1.1 on 2020-09-09 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200908_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='slug', editable=False),
        ),
    ]
