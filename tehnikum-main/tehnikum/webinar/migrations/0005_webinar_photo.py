# Generated by Django 4.1.4 on 2023-01-08 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webinar", "0004_alter_webinar_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="webinar",
            name="photo",
            field=models.ImageField(null=True, upload_to="pics"),
        ),
    ]
