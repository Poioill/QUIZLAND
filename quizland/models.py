from django.db import models


class Answers(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Quiz_links(models.Model):
    item = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=25, default='some_value')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.item


class Quiz_items(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title
