from django.db import models
from django.db.models.fields import CharField, DateTimeField

class Booklist(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length = 100, null=True)
    tag = models.CharField(max_length=100, null=True)
    tag_secodne = models.CharField(max_length=10, null=True)
    second = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'booklist'