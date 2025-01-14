# Generated by Django 4.0.6 on 2024-04-05 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LEI', '0003_disciplina_linguagens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='disciplina',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='projeto_disciplina', to='LEI.disciplina'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='linguagens',
            field=models.ManyToManyField(related_name='projetos', to='LEI.linguagemdeprogramacao'),
        ),
    ]
