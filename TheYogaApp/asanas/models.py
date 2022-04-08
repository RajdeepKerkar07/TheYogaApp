from django.db import models


class Asana(models.Model):
    name = models.CharField(max_length=256)
    problems = models.ManyToManyField("problems.Problems")

    def __str__(self):
        return self.name
