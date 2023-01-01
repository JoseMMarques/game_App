# Generated by Django 3.2.16 on 2022-12-29 15:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Designação')),
                ('code', models.CharField(blank=True, help_text='Introduza um código com 6 dígitos.', max_length=10, validators=[django.core.validators.RegexValidator(message='O código da Escola deve ter 6 dígitos.', regex='\\d{6}$')], verbose_name='Código de Agrupamento')),
                ('slug', models.SlugField(blank=True, help_text='Deixar em branco para criar um slug automático e único', max_length=255, unique=True)),
                ('address', models.TextField(blank=True, verbose_name='Morada')),
                ('phone1', models.CharField(blank=True, max_length=12, verbose_name='Telefone 1')),
                ('phone2', models.CharField(blank=True, max_length=12, verbose_name='Telefone 2')),
                ('nif', models.CharField(blank=True, help_text='Introduza um NIF com 9 dígitos.', max_length=10, validators=[django.core.validators.RegexValidator(message='o NIF deve ter 9 dígitos.', regex='\\d{9}$')], verbose_name='NIF')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now_add=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Escola',
                'verbose_name_plural': 'Escolas',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Insira um ano letivo como o formato "aaaa/aaaa. Exemplo: 2022/2023', max_length=12, validators=[django.core.validators.RegexValidator(message='Formato "aaaa/aaaa. Exemplo: 2022/2023', regex='^\\d{4}\\/\\d{4}$')], verbose_name='Designação')),
                ('slug', models.SlugField(blank=True, help_text='Deixar em branco para criar um slug automático e único', max_length=20, unique=True)),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Início')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Fim')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now_add=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Ano Letivo',
                'verbose_name_plural': 'Anos Letivos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Designação da turma')),
                ('grade', models.CharField(choices=[('1ºANO', '1ºAno'), ('2ºANO', '2ºAno'), ('3ºANO', '3ºAno'), ('4ºANO', '4ºAno'), ('5ºANO', '5ºAno'), ('6ºANO', '6ºAno'), ('7ºANO', '7ºAno'), ('8ºANO', '8ºAno'), ('9ºANO', '9ºAno'), ('PRE', 'Pre-escola')], default='9ºAno', max_length=12, verbose_name='Ano de Escolaridade')),
                ('slug', models.SlugField(blank=True, help_text='Deixar em branco para criar um slug automático e único.', max_length=255, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_structure.school', verbose_name='Escola')),
                ('school_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_structure.schoolyear', verbose_name='Ano Letivo')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
                'ordering': ('name',),
            },
        ),
    ]
