from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
class StringRun(models.Model):
    title_text = models.CharField(max_length=100, verbose_name='Enter your title text')
    description_text = models.TextField(verbose_name='Enter your description text')

    def __str__(self):
        return self.title_text

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class FilmModel(models.Model):
    GENRE = (
        ('Horror', 'Horror'),
        ('Comedy', 'Comedy')
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='film/')
    cost = models.PositiveIntegerField()
    genre = models.CharField(max_length=100, choices=GENRE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'


class AfishaTable(models.Model):
    film_name = models.CharField(max_length=100, verbose_name='enter your film name')
    time_hall = models.TimeField(verbose_name='enter this time')
    hall = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

    def __str__(self):
        return self.film_name


class Slider(models.Model):
    slide = models.URLField()


class ReviewModel(models.Model):
    film_object = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name='comment_object')
    mark = models.PositiveIntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    text_review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.film_object}-{self.mark}'