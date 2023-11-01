# Generated by Django 4.2.5 on 2023-10-25 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Djangoapp', '0003_remove_news_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Номер группы')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Лекция', 'verbose_name_plural': 'Лекции'},
        ),
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
        migrations.RemoveField(
            model_name='news',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='news',
            name='photo',
        ),
        migrations.AlterField(
            model_name='news',
            name='short_dest',
            field=models.CharField(max_length=255, verbose_name='Тема лекции'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название предмета'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='news',
            name='groups',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Djangoapp.groups', verbose_name='Группа'),
        ),
    ]
