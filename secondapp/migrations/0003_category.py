# Generated by Django 2.2 on 2020-05-30 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0002_statement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50)),
                ('cover_pic', models.FileField(upload_to='media')),
                ('description', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]