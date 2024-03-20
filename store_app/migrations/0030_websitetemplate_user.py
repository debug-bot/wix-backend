# Generated by Django 3.2.8 on 2024-03-20 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store_app', '0029_alter_customcollection_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitetemplate',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.user'),
            preserve_default=False,
        ),
    ]
