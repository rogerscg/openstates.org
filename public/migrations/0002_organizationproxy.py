# Generated by Django 2.0.9 on 2018-12-29 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0004_auto_20171005_2028"), ("public", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="OrganizationProxy",
            fields=[],
            options={"proxy": True, "indexes": []},
            bases=("core.organization",),
        )
    ]
