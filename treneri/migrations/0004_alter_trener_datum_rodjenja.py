# Generated by Django 4.0.4 on 2022-06-29 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treneri', '0003_remove_trener_godiste_trener_datum_rodjenja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trener',
            name='datum_rodjenja',
            field=models.DateField(),
        ),
    ]