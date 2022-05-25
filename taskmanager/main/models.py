from django.db import models
from datetime import datetime


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

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Reviews(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    description = models.TextField('Описание')
    time = models.DateTimeField('Время написания', default=datetime.now)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Cuisine(models.Model):
    name = models.TextField('Название кухни')
    task = models.ManyToManyField(Task)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кухня'
        verbose_name_plural = 'Кухни'


class Grade(models.Model):
    val = models.IntegerField('Оценка пользователя')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __int__(self):
        return self.val

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
