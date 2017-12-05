# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class GeneDataBank(models.Model):
    class Meta:
        managed = False
        db_table = 'gene_autocomplete'

    species = models.CharField(max_length=255, blank=True, null=True)
    stable_id = models.CharField(max_length=128, primary_key=True)
    display_label = models.CharField(max_length=128, blank=True, null=True)
    location = models.CharField(max_length=60, blank=True, null=True)
    source_db = models.CharField(max_length=32, db_column='db')
