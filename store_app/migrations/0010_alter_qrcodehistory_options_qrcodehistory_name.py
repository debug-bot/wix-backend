# Generated by Django 4.2.11 on 2024-03-24 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store_app", "0009_qrcodehistory"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="qrcodehistory",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddField(
            model_name="qrcodehistory",
            name="name",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
