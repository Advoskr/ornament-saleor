# Generated by Django 3.2.21 on 2023-10-13 09:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0176_alter_orderevent_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="voucher_code",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
