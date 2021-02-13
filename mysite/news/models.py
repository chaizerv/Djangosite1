from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    аnons = models.CharField('Анонс', max_length=150)
    full_text = models.TextField('Статья')
    created_at = models.DateTimeField('Дата публикации', null = True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

