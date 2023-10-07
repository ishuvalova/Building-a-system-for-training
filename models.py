from django.db import models
from django.http import HttpResponse


class Lesson(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    url = models.URLField()
    duration = models.DurationField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class Product(models.Model):

    title = models.CharField(max_length=50)
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class User(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    lesson = models.ManyToManyField(Lesson, related_name="lessons")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Owner(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="the related product")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"









