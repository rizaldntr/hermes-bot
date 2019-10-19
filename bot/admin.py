from django.contrib import admin

from .models import TransportDetail, ScheduleDetail, User, StopDetail, TrackDetail

# Register your models here.
admin.site.register(TransportDetail)
admin.site.register(ScheduleDetail)
admin.site.register(StopDetail)
admin.site.register(TrackDetail)
admin.site.register(User)