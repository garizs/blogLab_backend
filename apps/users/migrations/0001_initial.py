# Generated by Django 3.2.7 on 2022-01-10 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user', verbose_name='Пользователь')),
                ('profile_picture', models.ImageField(default='users/default.svg', upload_to='users', verbose_name='Аватарка пользователя')),
                ('is_banned', models.BooleanField(default=False, verbose_name='Забаненный')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Админ')),
                ('is_editor', models.BooleanField(default=False, verbose_name='Редактор')),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профили пользователей',
            },
        ),
    ]
