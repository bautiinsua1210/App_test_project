# Generated by Django 4.1.3 on 2022-12-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTest', '0002_remove_family_born_date_remove_family_surname'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='surname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]