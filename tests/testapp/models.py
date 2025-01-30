from django.db import models

from datetimeutc.fields import DateTimeUTCField


class TestModel(models.Model):
    __test__ = False

    name = models.CharField(max_length=100)  # type: ignore
    time_auto_added = DateTimeUTCField(auto_now_add=True)
    time_auto_updated = DateTimeUTCField(auto_now=True)
    time_set_manually = DateTimeUTCField(null=True)
