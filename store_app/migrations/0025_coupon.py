# Generated by Django 3.2.8 on 2021-12-16 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0024_customcollection_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(default='', max_length=256)),
                ('code', models.CharField(default='', max_length=256)),
                ('taken', models.BooleanField(default=False)),
                ('discount_type', models.CharField(choices=[('POR CIENTO', 'POR CIENTO'), ('FIJO', 'FIJO')], default='POR CIENTO', max_length=256)),
                ('discount', models.FloatField(default=0.0)),
                ('how_many_items', models.IntegerField(default=0)),
            ],
        ),
    ]
