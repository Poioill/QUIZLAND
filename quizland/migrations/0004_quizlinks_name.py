# Generated by Django 4.1.3 on 2022-11-27 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizland', '0003_quizlinks'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizlinks',
            name='name',
            field=models.CharField(default='some_value', max_length=25),
        ),
    ]
