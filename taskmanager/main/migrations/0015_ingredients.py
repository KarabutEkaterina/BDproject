# Generated by Django 4.0.4 on 2022-05-29 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=100)),
                ('description', models.TextField(verbose_name='Описание')),
                ('cuisine', models.ManyToManyField(to='main.cuisine')),
            ],
        ),
    ]