# Generated by Django 4.0.6 on 2024-05-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='resumo',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='autor',
            name='imagem',
            field=models.ImageField(default='blog/default.jpg', null=True, upload_to='blog/'),
        ),
    ]