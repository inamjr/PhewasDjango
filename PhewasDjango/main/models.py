from django.db import models

# Create your models here.

class PheWasModel(models.Model):
    lab_name = models.CharField(max_length=100)
    analysis_type = models.CharField(max_length=100)
    char = models.IntegerField(max_length=20)
    pos = models.IntegerField(max_length=200)
    marker_name = models.CharField(max_length=200)
    rsid = models.CharField(max_length=200)
    ref = models.CharField(max_length=50)
    alt = models.CharField(max_length=50)
    effect = models.CharField(max_length=200)
    analysis_efect = models.IntegerField(max_length=200)
    var = models.IntegerField(max_length=200)
    direction = models.CharField(max_length=2)
    std_err = models.IntegerField(max_length=200)
    gene = models.CharField(max_length=200)
    log_p = models.IntegerField(max_length=200)
    p = models.IntegerField(max_length=200)

    def __str__(self):
	    return self.lab_name