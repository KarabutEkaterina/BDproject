from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'


class Place(models.Model):
    task = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    address = models.CharField("Адрес", max_length=80)

    def __str__(self):
        return self.address


class Reviews(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    description = models.TextField('Описание')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
