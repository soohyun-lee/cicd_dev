from django.db import models
from django.db.models.fields import CharField

class Booklist(models.Model):
    name = CharField(max_length=100, null=True)
    category = CharField(max_length=40, null=True)

    class Meta:
        db_table = 'bookList'