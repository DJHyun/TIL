from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.TextField()


class Movie(models.Model):
    title = models.TextField()
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Score(models.Model):
    content = models.TextField()
    score = models.IntegerField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)


