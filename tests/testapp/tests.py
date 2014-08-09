import datetime
from dateutil import tz
from django.conf import settings
from django.test import TestCase
from django.utils import timezone
from testapp.models import TestModel


class ModelTests(TestCase):

    def setUp(self):
        self.local_now = datetime.datetime.now().replace(tzinfo=tz.gettz(
            settings.TIME_ZONE))
        self.utc_now = self.local_now.astimezone(tz.gettz('UTC'))
        self.test_model = TestModel.objects.create(
            name='Test', time_set_manually=self.utc_now
        )

    def test_auto_add_now_works_as_expected(self):
        self.assertTrue(timezone.is_aware(self.test_model.time_auto_added))
        self.assertEqual(
            self.test_model.time_auto_added.tzinfo.utcoffset(
                self.test_model.time_auto_added), datetime.timedelta(0))

    def test_auto_add_works_as_expected(self):
        self.test_model.name = 'Updating name'
        self.test_model.save()

        self.assertTrue(timezone.is_aware(self.test_model.time_auto_updated))
        self.assertGreater(self.test_model.time_auto_updated,
                           self.test_model.time_auto_added)
        self.assertEqual(
            self.test_model.time_auto_updated.tzinfo.utcoffset(
                self.test_model.time_auto_updated), datetime.timedelta(0))

    def test_manually_set_datetime_is_saved_as_utc(self):
        self.assertTrue(timezone.is_aware(self.test_model.time_set_manually))
        self.assertEqual(self.test_model.time_set_manually, self.utc_now)
        self.assertEqual(
            self.test_model.time_set_manually.tzinfo.utcoffset(
                self.test_model.time_set_manually), datetime.timedelta(0))

    def test_saved_datetime_is_converted_to_localtime_correctly(self):
        self.assertEqual(
            self.test_model.time_set_manually.astimezone(
                tz.gettz(settings.TIME_ZONE)),
            self.local_now
        )

    def test_null_datetime_value_is_supported(self):
        another_test_model = TestModel.objects.create(name='Test 2')
        self.assertIsNone(another_test_model.time_set_manually)
