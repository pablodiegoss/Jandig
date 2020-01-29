# Generated by Django 2.2.2 on 2020-01-27 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_exhibit_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibit',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='exhibits', to='users.Profile'),
        ),
    ]
