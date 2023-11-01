from django.db import models

class Articles(models.Model):
    title = models.CharField('Название',max_length=50, default='Новость')
    anons = models.CharField('Анонс',max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата Публикации')
    photo = models.ImageField(upload_to='images/', verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'