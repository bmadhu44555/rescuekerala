# Generated by Django 2.1 on 2018-08-21 18:29

from django.db import migrations, models
import mainapp.utils.model_utils


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0070_merge_20180821_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvFileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('csv_file', models.FileField(upload_to=mainapp.utils.model_utils.upload_to)),
            ],
        ),
    ]
