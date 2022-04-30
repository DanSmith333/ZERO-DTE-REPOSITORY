from django.db import models

# Create your models here.
class Oscarrr(models.Model):
    expiration_date = models.CharField(max_length=10)
    symbol = models.CharField('SPX', max_length=6, default='SPX')
    min_R2R = models.IntegerField(default=5)
    max_loss = models.IntegerField(default=-150)
    min_distance = models.IntegerField(default=0)
    max_distance = models.IntegerField(default=50)
    min_base = models.IntegerField(default=20)
    max_base = models.IntegerField(default=100)
    BF = models.BooleanField(default=True)
    UF = models.BooleanField(default=True)
    IF = models.BooleanField(default=False)
    IC = models.BooleanField(default=False)
    CN = models.BooleanField(default=False)
    es_spx_difference = models.IntegerField(default=-10)
    es_option = models.CharField(max_length=17, default=' (EOM) /EW22:XCE ')
    es_symbol = models.CharField(max_length=16, default='/ESH22:XCME 1/50')

    def __str__(self):
        return self.symbol