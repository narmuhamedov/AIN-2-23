from django.db import models

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