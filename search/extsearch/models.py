from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class Step(models.Model):
    lesson = models.ForeignKey(Lesson)
    text = models.CharField(max_length=50000)

    def __str__(self):
        return self.text


