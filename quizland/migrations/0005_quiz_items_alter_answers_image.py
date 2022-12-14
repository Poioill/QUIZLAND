# Generated by Django 4.1.3 on 2022-11-29 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizland', '0004_quizlinks_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('image', models.ImageField(upload_to='')),
                ('topic', models.CharField(max_length=20)),
                ('sub_topic', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='answers',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
