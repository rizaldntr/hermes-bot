from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    display_name = models.CharField(max_length=100)
    picture_url = models.CharField(max_length=100)
    status_message = models.TextField()

class TransportDetail(models.Model):
    transport_name = models.CharField(max_length=100)
    transport_name_plural = models.CharField(max_length=100)

class ScheduleDetail(models.Model):
    icon = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    long_name = models.CharField(max_length=100)
    schedule_id = models.CharField(max_length=100, primary_key=True)
    transport_id = models.CharField(max_length=100)
    validity = models.CharField(max_length=100, null=True)
    transport_detail = models.ForeignKey(TransportDetail, on_delete=models.PROTECT)

class StopDetail(models.Model):
    area_name = models.CharField(max_length=100, null=True)
    direction_name = models.CharField(max_length=100, null=True)
    icon = models.CharField(max_length=100)
    stop_detail_id = models.CharField(max_length=100, primary_key=True)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    map_icon = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

class TrackDetail(models.Model):
    direction = models.IntegerField()
    track_detail_id = models.CharField(max_length=100, primary_key=True)
    is_hidden = models.BooleanField()
    name = models.CharField(max_length=100)
    shape = models.TextField()
    destination = models.CharField(max_length=100)
    stops = models.ManyToManyField(StopDetail)
    schedule_detail = models.ForeignKey(ScheduleDetail, on_delete=models.PROTECT)