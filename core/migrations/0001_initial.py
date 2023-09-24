# Generated by Django 3.2.13 on 2023-09-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbPragas',
            fields=[
                ('id_praga', models.AutoField(primary_key=True, serialize=False)),
                ('cultura', models.CharField(blank=True, max_length=45, null=True)),
                ('especie', models.CharField(blank=True, max_length=45, null=True)),
                ('nome_comum', models.CharField(max_length=45)),
                ('nome_comum2', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Tabela de Praga',
                'verbose_name_plural': 'Tabela de Pragas',
            },
        ),
    ]
