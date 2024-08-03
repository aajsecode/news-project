from django.db import models


# Create your models here.
class Page(models.Model):
    url = models.CharField(max_length=200)
    views = models.IntegerField()

    def __str__(self) -> str:
        return self.url
