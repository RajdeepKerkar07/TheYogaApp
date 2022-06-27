from django.db import models


class Diet(models.Model):
    problem = models.OneToOneField("problems.Problems", on_delete=models.CASCADE)
    tips = models.TextField()

    def __str__(self):
        return self.problem.name

    def tips_list(self):
        return self.tips.split('\n')
