# Generated by Django 3.0.3 on 2021-05-24 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdg', '0004_auto_20210522_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='proses',
            name='bpmn_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]