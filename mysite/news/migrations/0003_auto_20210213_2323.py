# Generated by Django 3.1.6 on 2021-02-13 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210213_2252'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='articles',
            name='аnons',
            field=models.CharField(default='', max_length=150, verbose_name='Анонс'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articles',
            name='created_at',
            field=models.DateTimeField(null=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]
