Django DateTimeUTC
==================

django-datetime-utc provides ``DateTimeUTCField``, a naive datetime model field.
In PostgreSQL this translates to the field *timestamp without time zone*.
All timestamps are saved in UTC.


Why use this?
-------------
The problem with using Django's ``DateTimeField`` is unless the default timezone
on your (PostgreSQL) database server is set to UTC it doesn't matter which TZ
settings you select in Django, PostgreSQL will save all timestamps in local time
with an offset.

Features
--------

- Supports the default ``DateTimeField`` options such as ``auto_now_add`` and ``auto_now``
- Works with South
- Saves all timestamps in UTC
- Values automatically converted to local time (specified by ``TIME_ZONE`` in your project settings.py) in forms and templates

Install
-------
From PyPi:
::

    $ pip install django-datetime-utc

In ``settings.py`` add ``datetimeutc`` to the list of installed apps, set your
local time zone and ensure time zone support is enabled:
::

    TIME_ZONE = 'Europe/London'
    USE_TZ = True
    INSTALLED_APPS = (
        #...
        'datetimeutc',
    )

Usage
-----
In ``models.py``:
::

    from django.db import models
    from datetimeutc.fields import DateTimeUTCField

    class Stuff(models.Model):
        title = models.CharField(max_length=100)
        stuff_time = DateTimeUTCField()
        submitted = DateTimeUTCField(auto_now_add=True)

Notes
-----

If your code creates datetime objects, they should always be TZ aware so they
are automatically converted correctly to UTC (if necessary) before being saved
to the database. Using the ``Stuff`` model above as an example, to set
``stuff_time`` correctly you would:
::

    import datetime
    from dateutil import tz

    utcnow = datetime.datetime.utcnow().replace(tzinfo=tz.gettz('UTC'))
    Stuff.objects.create(title='My stuff', stuff_time=utcnow)

This also goes for user defined datetime objects. For example in the admin
panel, if the user submits a value for ``stuff_time``, in ``admin.py`` you
would:
::

    from dateutil import tz
    from django.contrib import admin
    from django.conf import settings
    from stuff.models import Stuff


    class StuffAdmin(admin.ModelAdmin):
        def save_model(self, request, obj, form, change):
            obj.stuff_time = obj.stuff_time.replace(
                tzinfo=tz.gettz(settings.TIME_ZONE))
            obj.save()

    admin.site.register(Stuff, StuffAdmin)

Here the datetime object is made TZ aware by setting the time zone to the
one specified in ``settings.py`` (presumably the time zone of the user
entering this data). This will be converted to UTC prior to save automatically.
