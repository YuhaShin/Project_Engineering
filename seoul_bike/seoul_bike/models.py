# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MonthTimeUsage(models.Model):
    base_mn = models.CharField(max_length=2, db_collation='utf8_general_ci', blank=True, null=True)
    base_tm = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    usage_amt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'month_time_usage'


class MonthUsage(models.Model):
    date = models.CharField(max_length=7, db_collation='utf8mb4_general_ci', blank=True, null=True)
    s = models.DecimalField(max_digits=42, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'month_usage'


class PopulUsage(models.Model):
    base_tm = models.IntegerField()
    usage_amt = models.DecimalField(max_digits=46, decimal_places=4, blank=True, null=True)
    life_popul = models.FloatField(blank=True, null=True)
    bus_popul = models.FloatField(blank=True, null=True)
    sub_popul = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'popul_usage'


class RainUsage06(models.Model):
    base_dt = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    bike_usage = models.DecimalField(max_digits=42, decimal_places=0, blank=True, null=True)
    rain_amt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rain_usage_06'


class StationUsage(models.Model):
    station_id = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    rent_amt = models.DecimalField(max_digits=41, decimal_places=0, blank=True, null=True)
    return_amt = models.DecimalField(max_digits=41, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station_usage'


class TimeUsage(models.Model):
    use_tm = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    bikeusage = models.DecimalField(max_digits=46, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_usage'
