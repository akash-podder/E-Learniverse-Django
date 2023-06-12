from django.db import models

from notification_app.validators import MOBILE_VALIDATOR


# Create your models here.
class RegisteredAndroidUser(models.Model):
    mobile = models.CharField(max_length=11, validators=[MOBILE_VALIDATOR], unique=True, db_index=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    fcm_token = models.CharField(max_length=16384)

    class Meta:
        db_table = 'registered_android_users'

class NotificationSentRecord(models.Model):
    total_user_count = models.PositiveIntegerField()
    success_count = models.PositiveIntegerField()
    fail_count = models.PositiveIntegerField()
    sent_at = models.DateTimeField()

    class Meta:
        db_table = 'notification_records'