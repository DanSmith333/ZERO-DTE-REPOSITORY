from django.db import models

# Create your models here.


class Situation(models.Model):
    situation_text = models.CharField('Situation', max_length=500)
    def __str__(self):
        return self.situation_text

class Annoyance(models.Model):
    annoyance_text = models.CharField('Annoyance', max_length=500)
    def __str__(self):
        return self.annoyance_text
