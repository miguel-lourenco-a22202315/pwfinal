# Generated by Django 4.0.6 on 2024-04-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LEI', '0007_alter_projeto_disciplina'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='disciplina',
        ),
        migrations.AddField(
            model_name='projeto',
            name='disciplina',
            field=models.ManyToManyField(to='LEI.disciplina'),
        ),
    ]
