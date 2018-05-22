from django.db import models
import django_tables2 as tables


# Create your models here.
class DocumentTable(tables.Table):
        id = tables.Column()
        name = tables.Column()
        node = tables.Column()
        url = tables.URLColumn(text='Link Documento')
