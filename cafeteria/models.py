from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    plate = models.CharField(max_length=20, unique=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.plate})"


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.date.date()}"


class Branch(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author}: {self.content[:40]}"
