# Generated by Django 3.2.8 on 2024-03-23 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0007_rename_html_content4_usertemplate_html_content1'),
    ]

    operations = [
        migrations.AddField(
            model_name='templates',
            name='ecommerce',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='templates',
            name='html_content1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='templates',
            name='html_content2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='templates',
            name='html_content3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
