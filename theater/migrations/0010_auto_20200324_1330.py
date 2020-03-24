# Generated by Django 3.0.4 on 2020-03-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0009_auto_20200324_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='show_from_date',
            new_name='show_now_from_date',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='show_to_date',
            new_name='show_now_to_date',
        ),
        migrations.AddField(
            model_name='film',
            name='show_soon_from_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
