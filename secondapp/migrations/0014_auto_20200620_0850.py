# Generated by Django 2.2 on 2020-06-20 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0013_auto_20200620_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
