# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-19 14:59


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_type_gating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenttypegatingconfig',
            name='enabled_as_of',
            field=models.DateField(blank=True, default=None, help_text='If the configuration is Enabled, then all enrollments created after this date (UTC) will be affected.', null=True, verbose_name='Enabled As Of'),
        ),
        migrations.AlterField(
            model_name='contenttypegatingconfig',
            name='studio_override_enabled',
            field=models.NullBooleanField(default=None, help_text='Allow Feature Based Enrollment visibility to be overriden on a per-component basis in Studio.', verbose_name='Studio Override Enabled'),
        ),
    ]