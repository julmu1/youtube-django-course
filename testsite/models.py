from django.db import models

class TestData(models.Model):
    location = models.CharField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.location} from {self.year}'