# Generated by Django 2.2 on 2020-06-02 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0005_auto_20200601_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_id',
            field=models.IntegerField(default=1),
        ),
    ]
