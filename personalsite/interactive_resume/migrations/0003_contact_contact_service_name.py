# Generated by Django 3.1.3 on 2020-11-23 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactive_resume', '0002_auto_20201123_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_service_name',
            field=models.CharField(default='delete', max_length=200),
            preserve_default=False,
        ),
    ]