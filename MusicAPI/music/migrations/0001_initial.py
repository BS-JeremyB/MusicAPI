# Generated by Django 5.1.1 on 2024-09-27 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('performer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('genre', models.CharField(max_length=255)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='music.album')),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performer.band')),
            ],
        ),
        migrations.CreateModel(
            name='MusicArtist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=255, null=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performer.artist')),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.music')),
            ],
        ),
        migrations.AddField(
            model_name='music',
            name='artists',
            field=models.ManyToManyField(related_name='tracks', through='music.MusicArtist', to='performer.artist'),
        ),
    ]
