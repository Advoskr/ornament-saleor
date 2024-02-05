# Generated by Django 1.11.5 on 2018-01-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("site", "0010_auto_20171113_0958")]

    operations = [
        migrations.AlterField(
            model_name="authorizationkey", name="key", field=models.TextField()
        ),
        migrations.AlterField(
            model_name="authorizationkey",
            name="name",
            field=models.CharField(
                choices=[
                    ("facebook", "Facebook-Oauth2"),
                    ("google-oauth2", "Google-Oauth2"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="authorizationkey", name="password", field=models.TextField()
        ),
        migrations.AlterField(
            model_name="sitesettings",
            name="description",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name="sitesettings",
            name="header_text",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
