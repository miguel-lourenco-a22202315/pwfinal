# Generated by Django 4.0.6 on 2024-05-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0007_remove_musicas_biografia_bandas_biografia'),
    ]

    operations = [
        migrations.AddField(
            model_name='bandas',
            name='descricaocompleta',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='bandas',
            name='imagemintegrantes',
            field=models.ImageField(default='bandas/default.jpg', null=True, upload_to='bandas/'),
        ),
    ]