# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20151211_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=254)),
                ('description', models.TextField()),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subscription_end', models.DateTimeField(default=datetime.datetime(2015, 12, 14, 12, 3, 50, 910369, tzinfo=utc))),
                ('magazine', models.ForeignKey(to='accounts.Magazine')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 14, 12, 3, 50, 904674, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(related_name='purchases', to=settings.AUTH_USER_MODEL),
        ),
    ]
