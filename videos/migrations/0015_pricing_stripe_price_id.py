# Generated by Django 3.1 on 2020-09-06 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0014_auto_20200905_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing',
            name='stripe_price_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]