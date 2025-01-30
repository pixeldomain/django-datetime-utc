# Django DateTimeUTC

[![CI and unit tests](https://github.com/pixeldomain/django-datetime-utc/actions/workflows/ci.yml/badge.svg)](https://github.com/pixeldomain/django-datetime-utc/actions/workflows/ci.yml)

django-datetime-utc provides `DateTimeUTCField`, a naive datetime model field. In PostgreSQL this translates to the field *timestamp without time zone*. All timestamps are saved in UTC.


## Why use this?

The problem with using Django's `DateTimeField` is unless the default timezone on your (PostgreSQL) database server is set to UTC it doesn't matter which TZ settings you select in Django, PostgreSQL will save all timestamps in local time with an offset.

## Features

- Supports the default `DateTimeField` options such as `auto_now_add` and `auto_now`
- Saves all timestamps in UTC
- Values automatically converted to local time (specified by `TIME_ZONE` in your project `settings.py`) in forms and templates

## Install

From PyPi:

```bash
pip install django-datetime-utc
```

In `settings.py` add `datetimeutc` to the list of installed apps, set your local time zone and ensure time zone support is enabled:

```python
TIME_ZONE = 'Europe/London'
USE_TZ = True
INSTALLED_APPS = (
    #...
    'datetimeutc',
)
```

## Usage

In `models.py`:

```python
from django.db import models
from datetimeutc.fields import DateTimeUTCField

class Journey(models.Model):
    name = models.CharField(max_length=100)
    departure_time = DateTimeUTCField(null=True)
    arrival_time = DateTimeUTCField(null=True)
    record_created = DateTimeUTCField(auto_now_add=True)
```

## Notes

If your code creates datetime objects, they should always be TZ aware so they are automatically converted correctly to UTC (if necessary) before being saved to the database.

Using the `Journey` model above as an example, to set `departure_time` correctly you would:

```python
import datetime
from zoneinfo import ZoneInfo

departure_time = datetime.datetime.now(datetime.UTC)

# or user defined (naive) datetime objects
departure_time = user_datetime.replace(tzinfo=ZoneInfo(settings.TIME_ZONE))

Journey.objects.create(name='Flight to LA', departure_time=departure_time)
```
