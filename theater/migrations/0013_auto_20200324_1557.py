# Generated by Django 3.0.4 on 2020-03-24 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0012_auto_20200324_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='image',
        ),
        migrations.AddField(
            model_name='film',
            name='poster',
            field=models.ImageField(default='uploads/None/no-img.jpg', upload_to='uploads/film/film-poster'),
        ),
        migrations.CreateModel(
            name='FilmGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='uploads/None/no-img.jpg', upload_to='uploads/film/film-gallery')),
                ('film', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='theater.Film')),
            ],
        ),
    ]
