from django.db import models

# Create your models here.




class Parameters(models.Model):
    begin_balance = models.FloatField(default=10000)
    position_size = models.FloatField(default=1.5)
    def __str__(self):
        return 'Beginnig Balance=' + str(self.begin_balance) + ',   Position Size=' + str(self.position_size) + '%'


class Assumptions(models.Model):
    assumption_number = models.IntegerField(default=0)
    hit_rate = models.IntegerField(default=20)
    low_end = models.IntegerField(default=0)
    high_end = models.IntegerField(default=0)
    def __str__(self):
        return 'Hit Rate=' + str(self.hit_rate) + \
            ',   Low End=' + str(self.low_end) + \
            ',   High End=' + str(self.high_end) 


