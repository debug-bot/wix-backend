# Generated by Django 3.2.8 on 2024-03-23 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0005_auto_20240322_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertemplate',
            name='ecommerce',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usertemplate',
            name='html_content2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usertemplate',
            name='html_content3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usertemplate',
            name='html_content4',
            field=models.TextField(blank=True, null=True),
        ),
    ]
