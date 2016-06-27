# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('arbeitskraft', str(instance.id), filename)

class Arbeitskraft(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ausweisnummer = models.CharField(db_column='Ausweisnummer', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nachname = models.CharField(db_column='Nachname', max_length=50)  # Field name made lowercase.
    vorname = models.CharField(db_column='Vorname', max_length=50)  # Field name made lowercase.
    strasse = models.CharField(db_column='Strasse', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hausnummer = models.CharField(db_column='Hausnummer', max_length=5, blank=True, null=True)  # Field name made lowercase.
    plz = models.IntegerField(db_column='PLZ', blank=True, null=True)  # Field name made lowercase.
    foto = models.FileField( blank=True, null=True)  # Field name made lowercase.
    telefon = models.CharField(db_column='Telefon', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mobil = models.CharField(db_column='Mobil', max_length=30, blank=True, null=True)  # Field name made lowercase.
    beacon = models.ForeignKey('Beacon', models.DO_NOTHING, db_column='Beacon_ID')  # Field name made lowercase.
    firma = models.ForeignKey('Firma', models.DO_NOTHING, db_column='Firma_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'arbeitskraft'


class ArbeitskraftHasProjekt(models.Model):
    arbeitskraft = models.ForeignKey(Arbeitskraft, models.DO_NOTHING, db_column='Arbeitskraft_ID')  # Field name made lowercase.
    projekt = models.ForeignKey('Projekt', models.DO_NOTHING, db_column='Projekt_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'arbeitskraft_has_projekt'
        unique_together = (('arbeitskraft', 'projekt'),)


class Beacon(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    zuletzt_gesehen = models.DateTimeField(blank=True, null=True)
    letzter_boot = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beacon'


class Benutzer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nachname = models.CharField(db_column='Nachname', max_length=50)  # Field name made lowercase.
    vorname = models.CharField(db_column='Vorname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E-Mail', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hashed_password = models.CharField(db_column='Hashed_Password', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'benutzer'


class Firma(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, related_name='firmenname')  # Field name made lowercase.
    strasse = models.CharField(db_column='Strasse', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hausnummer = models.CharField(db_column='Hausnummer', max_length=5, blank=True, null=True)  # Field name made lowercase.
    plz = models.IntegerField(db_column='PLZ', blank=True, null=True)  # Field name made lowercase.
    telefon = models.CharField(db_column='Telefon', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'firma'


class Projekt(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'projekt'
