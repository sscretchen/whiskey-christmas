# Generated by Django 3.1.1 on 2020-09-12 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_post_slider_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]