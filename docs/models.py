from django.db import models
import datetime


class document(models.Model):
    
    docfile = models.FileField()