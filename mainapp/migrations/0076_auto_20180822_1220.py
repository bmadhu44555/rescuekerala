# Generated by Django 2.1 on 2018-08-22 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0075_person_unique_identifier"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="person",
            options={
                "verbose_name": "Relief: Inmate",
                "verbose_name_plural": "Relief: Inmates",
            },
        ),
    ]
