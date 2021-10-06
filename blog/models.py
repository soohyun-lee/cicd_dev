from django.db import models
from django.db.models.fields import CharField, DateTimeField

class Booklist(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length = 100)
    tag = models.CharField(max_length=100)
    tag_secodne = models.CharField(max_length=100)

    class Meta:
        db_table = 'booklist'