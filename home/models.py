from django.db import models

# Create your models here.
class Item(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=512)
    summary = models.TextField()
    date_published = models.DateTimeField()
    author = models.CharField(max_length=256)

    def __str__(self):
        return self.author