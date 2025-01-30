import datetime
from zoneinfo import ZoneInfo

from django.conf import settings
from django.db import models
from django.utils import timezone


# pylint: disable=unused-argument
class DateTimeUTCField(models.DateTimeField):
    """Create a DB timestamp field that is TZ naive."""

    description = "Date (with time and no time zone)"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        if connection.settings_dict["ENGINE"] == "django.db.backends.mysql":
            return "datetime"
        return "timestamp"

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        if isinstance(value, datetime.datetime):
            if settings.USE_TZ and timezone.is_naive(value):
                return value.replace(tzinfo=ZoneInfo("UTC"))
            return value
        return super().to_python(value)

    def get_prep_value(self, value):
        if isinstance(value, datetime.datetime):
            return value.astimezone(ZoneInfo("UTC"))
        return value
