# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20160111_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 13, 15, 49, 33, 738188, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 13, 15, 49, 33, 734735, tzinfo=utc)),
        ),
    ]
