# Generated by Django 2.2.6 on 2019-10-15 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_auto_20191015_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stopdetail',
            name='area_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stopdetail',
            name='direction_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]