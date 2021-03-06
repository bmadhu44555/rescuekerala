# Generated by Django 2.1 on 2018-08-11 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0008_auto_20180811_1127"),
    ]

    operations = [
        migrations.AddField(
            model_name="request",
            name="needtoilet",
            field=models.BooleanField(default=False, verbose_name="Toileteries"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="request",
            name="status",
            field=models.CharField(
                choices=[("new", "New"), ("pro", "In progess"), ("sup", "Supplied")],
                max_length=10,
            ),
        ),
    ]
