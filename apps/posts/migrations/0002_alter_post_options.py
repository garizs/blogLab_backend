# Generated by Django 3.2.7 on 2022-01-12 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['pk'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
