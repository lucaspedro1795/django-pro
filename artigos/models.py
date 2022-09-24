import datetime

from django.db import models
from django.utils import timezone


class Artigo(models.Model):
    Titulo = models.CharField(max_length=200)
    Rotulo = models.CharField(max_length=200)
    Problema = models.CharField(max_length=255)
    Solução = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
   
    
    def __str__(self):
        return self.Titulo
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)