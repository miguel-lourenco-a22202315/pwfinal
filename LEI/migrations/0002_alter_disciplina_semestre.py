# Generated by Django 4.0.6 on 2024-04-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LEI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='semestre',
            field=models.CharField(max_length=100),
        ),
    ]