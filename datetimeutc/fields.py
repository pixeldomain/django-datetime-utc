import datetime
from dateutil import tz
from django.db import models
from django.utils import timezone
from django.conf import settings


class DateTimeUTCField(models.DateTimeField):
    """Create a DB timestamp field that is TZ naive."""

    description = "Date (with time and no time zone)"

    def __init__(self, *args, **kwargs):
        super(DateTimeUTCField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        if connection.settings_dict['ENGINE'] == 'django.db.backends.mysql':
            return 'datetime'
        else:
            return 'timestamp'

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        if isinstance(value, datetime.datetime):
            if settings.USE_TZ and timezone.is_naive(value):
                return value.replace(tzinfo=tz.gettz('UTC'))
            return value
        return super(DateTimeUTCField, self).to_python(value)

    def get_prep_value(self, value):
        if isinstance(value, datetime.datetime):
            return value.astimezone(tz.gettz('UTC'))
        return value
