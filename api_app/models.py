from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Api(models.Model):
    name = models.CharField(max_length=64)
    rater = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name
