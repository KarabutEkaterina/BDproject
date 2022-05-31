from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


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
    val = models.IntegerField('Оценка пользователя', validators=[MinValueValidator(0),
                                                                 MaxValueValidator(5)])
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __int__(self):
        return self.val

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'


class Services(models.Model):
    description = models.TextField('Описание')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'services'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Event(models.Model):
    name = models.CharField('Название мероприятия', max_length=120)
    event_date = models.DateTimeField('Дата проведения мероприятия')
    venue = models.CharField('Место проведения', max_length=120)
    description = models.TextField('Описание')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'event'
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Menu(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    data = models.JSONField

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Ingredients(models.Model):
    cuisine = models.ManyToManyField(Cuisine)
    ingredient = models.CharField(max_length=100)
    description = models.TextField('Описание')

    def __str__(self):
        return self.ingredient
