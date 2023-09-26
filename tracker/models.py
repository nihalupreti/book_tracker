from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.title} {self.author} {self.genre} {self.rating}'