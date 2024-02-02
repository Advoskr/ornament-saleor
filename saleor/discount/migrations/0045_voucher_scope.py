# Generated by Django 3.2.21 on 2023-09-20 11:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("discount", "0044_auto_20230421_1018"),
    ]

    operations = [
        migrations.AddField(
            model_name="voucher",
            name="scope",
            field=models.CharField(
                choices=[("retail", "Retail"), ("corporate", "Corporate")],
                default="retail",
                max_length=20,
            ),
        ),
    ]