# Generated by Django 3.1.7 on 2021-04-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='STRIPE_PID',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='original_bag',
            field=models.TextField(default=''),
        ),
    ]
