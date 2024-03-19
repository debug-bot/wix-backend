# Generated by Django 3.2.8 on 2021-11-01 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0006_alter_productvariation_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('email', models.CharField(default='-1', max_length=256)),
                ('stripe_charge_id', models.CharField(max_length=50)),
                ('amount', models.FloatField(default=0.0)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='-1', max_length=256)),
                ('phone', models.CharField(default='-1', max_length=256)),
                ('address1', models.CharField(default='-1', max_length=256)),
                ('address2', models.CharField(default='-1', max_length=256)),
                ('user_first_name', models.CharField(default='-1', max_length=256)),
                ('user_last_name', models.CharField(default='-1', max_length=256)),
                ('ordered_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('ordered', models.BooleanField(default=False)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store_app.cart')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store_app.payment')),
            ],
        ),
    ]
