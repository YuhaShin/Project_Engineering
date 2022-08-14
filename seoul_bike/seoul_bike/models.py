# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BikeUsage(models.Model):
    row_id = models.BigIntegerField(primary_key=True)
    station_id = models.TextField(blank=True, null=True)
    use_dt = models.TextField(blank=True, null=True)
    use_tm = models.TextField(blank=True, null=True)
    rent_amt = models.BigIntegerField()
    return_amt = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'BIKE_USAGE'


class DongCode(models.Model):
    dong_cd = models.IntegerField(primary_key=True)
    dong_cd_8 = models.TextField(blank=True, null=True)
    dong_nm = models.TextField(blank=True, null=True)
    gu_cd = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DONG_CODE'


class DongPopul(models.Model):
    row_id = models.BigAutoField(primary_key=True)
    base_dt = models.DateField()
    base_tm = models.IntegerField()
    dong_cd = models.CharField(max_length=10)
    life_popul = models.FloatField()
    bus_popul = models.FloatField()
    sub_popul = models.FloatField()

    class Meta:
        managed = False
        db_table = 'DONG_POPUL'


class EventInfo(models.Model):
    row_id = models.BigIntegerField(primary_key=True)
    event_nm = models.TextField(blank=True, null=True)
    place_id = models.IntegerField()
    from_dt = models.DateField(blank=True, null=True)
    to_dt = models.DateField(blank=True, null=True)
    event_tm = models.TextField(blank=True, null=True)
    target_kb = models.TextField(blank=True, null=True)
    fare_amt = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EVENT_INFO'


class EventPlace(models.Model):
    place_id = models.IntegerField(primary_key=True)
    place_nm = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EVENT_PLACE'


class EventStation(models.Model):
    row_id = models.BigIntegerField(primary_key=True)
    place_id = models.BigIntegerField(blank=True, null=True)
    place_nm = models.TextField(blank=True, null=True)
    station_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EVENT_STATION'


class GuCode(models.Model):
    gu_cd = models.IntegerField(primary_key=True)
    gu_nm = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GU_CODE'


class GuRain(models.Model):
    row_id = models.BigAutoField(primary_key=True)
    gu_name = models.CharField(max_length=10)
    gu_cd = models.IntegerField()
    base_dt = models.DateField()
    base_tm = models.CharField(max_length=10)
    rain_amt = models.FloatField()

    class Meta:
        managed = False
        db_table = 'GU_RAIN'


class Test(models.Model):
    row_i = models.BigAutoField(primary_key=True)
    gu_name = models.CharField(max_length=10)
    gu_cd = models.IntegerField()
    base_dt = models.DateField()
    base_tm = models.CharField(max_length=10)
    rain_amt = models.FloatField()

    class Meta:
        managed = False
        db_table = 'TEST'


class TourPlace(models.Model):
    place_id = models.IntegerField(primary_key=True)
    place_nm = models.TextField()
    place_star = models.FloatField()

    class Meta:
        managed = False
        db_table = 'TOUR_PLACE'


class TourStation(models.Model):
    row_id = models.BigIntegerField(primary_key=True)
    place_id = models.BigIntegerField()
    place_nm = models.TextField()
    station_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TOUR_STATION'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BusCount(models.Model):
    station_id = models.TextField(blank=True, null=True)
    station_addr = models.TextField(blank=True, null=True)
    dong_cd = models.TextField(blank=True, null=True)
    bus_station_cnt = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_count'


class CultureCount(models.Model):
    station_id = models.TextField(blank=True, null=True)
    station_addr = models.TextField(blank=True, null=True)
    dong_cd = models.TextField(blank=True, null=True)
    culture_place_cnt = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'culture_count'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EventCount(models.Model):
    station_id = models.TextField(blank=True, null=True)
    station_addr = models.TextField(blank=True, null=True)
    dong_cd = models.TextField(blank=True, null=True)
    event_place_cnt = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_count'


class MallCount(models.Model):
    station_id = models.TextField(blank=True, null=True)
    station_addr = models.TextField(blank=True, null=True)
    dong_cd = models.TextField(blank=True, null=True)
    mall_cnt = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_count'


class ParkCount(models.Model):
    station_id = models.TextField(blank=True, null=True)
    station_addr = models.TextField(blank=True, null=True)
    dong_cd = models.TextField(blank=True, null=True)
    park_cnt = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'park_count'


class RoadCount(models.Model):
    station_id = models.TextField(blank=True, null=True)
    station_addr = models.TextField(blank=True, null=True)
    dong_cd = models.TextField(blank=True, null=True)
    bike_road_cnt = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'road_count'


class SchoolCount(models.Model):
    station_id = models.TextField(blank=True, null=True)
    station_addr = models.TextField(blank=True, null=True)
    dong_cd = models.TextField(blank=True, null=True)
    school_cnt = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_count'


class StationNear(models.Model):
    station_id = models.IntegerField(primary_key=True)
    station_addr = models.TextField(blank=True, null=True)
    dong_cd = models.TextField(blank=True, null=True)
    bus_cnt = models.BigIntegerField(blank=True, null=True)
    culture_cnt = models.BigIntegerField(blank=True, null=True)
    event_cnt = models.BigIntegerField(blank=True, null=True)
    mall_cnt = models.BigIntegerField(blank=True, null=True)
    park_cnt = models.BigIntegerField(blank=True, null=True)
    road_cnt = models.BigIntegerField(blank=True, null=True)
    school_cnt = models.BigIntegerField(blank=True, null=True)
    sub_cnt = models.BigIntegerField(blank=True, null=True)
    tour_cnt = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station_near'


class SubCount(models.Model):
    station_id = models.TextField(blank=True, null=True)
    station_addr = models.TextField(blank=True, null=True)
    dong_cd = models.TextField(blank=True, null=True)
    subway_station_cnt = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_count'


class TourCount(models.Model):
    station_id = models.TextField(blank=True, null=True)
    station_addr = models.TextField(blank=True, null=True)
    dong_cd = models.TextField(blank=True, null=True)
    tour_place_cnt = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour_count'
