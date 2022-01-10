# Generated by Django 3.2.7 on 2022-01-10 01:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок статьи')),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('text', models.TextField(default='Hello, World!', verbose_name='Текст статьи')),
                ('post_type', models.CharField(choices=[('MAIN', 'Главная'), ('COOK', 'Кулинария'), ('FASHION', 'Мода'), ('HOT', 'Горячее'), ('BLOGGERS', 'Блоггеры')], max_length=15, verbose_name='Категория статьи')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
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
        migrations.CreateModel(
            name='PostPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='', upload_to='posts', verbose_name='Изображение')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='blog.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Картинка статьи',
                'verbose_name_plural': 'Картинки статьи',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.userprofile', verbose_name='Автор статьи'),
        ),
        migrations.CreateModel(
            name='FavouritePosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Пост')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.userprofile', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Избранный пост',
                'verbose_name_plural': 'Избранные посты',
            },
        ),
    ]
