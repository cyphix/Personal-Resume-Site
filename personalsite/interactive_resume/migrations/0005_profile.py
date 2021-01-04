# Generated by Django 3.1.3 on 2020-12-04 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactive_resume', '0004_auto_20201125_0838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('about', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
