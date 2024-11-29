# Generated by Django 3.2.23 on 2024-01-19 08:52

from django.db import migrations

from saleor.utils.migrations import form_alter_timestamp_column_sql


class Migration(migrations.Migration):
    dependencies = [
        ("page", "0028_add_default_page_type"),
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                f"""
            {form_alter_timestamp_column_sql("page_page", "created_at")}
            {form_alter_timestamp_column_sql("page_page", "published_at")}
            """
            ],
            reverse_sql=[
                f"""
            {form_alter_timestamp_column_sql("page_page", "created_at", True)}
            {form_alter_timestamp_column_sql("page_page", "published_at", True)}
            """
            ],
        ),
    ]