# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-29 01:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kynd', models.CharField(choices=[('P', 'PRINCIPAL'), ('C', 'COBRANÇA'), ('E', 'ENTREGA')], max_length=1, verbose_name='Tipo')),
                ('public_place', models.CharField(max_length=150, verbose_name='Logradouro')),
                ('number', models.CharField(max_length=150, verbose_name='Número')),
                ('city', models.CharField(max_length=150, verbose_name='Cidade')),
                ('state', models.CharField(max_length=150, verbose_name='Estado')),
                ('zipcode', models.CharField(max_length=10, verbose_name='Cep')),
                ('country', models.CharField(max_length=150, verbose_name='País')),
                ('phone', models.CharField(max_length=50, verbose_name='Fone')),
            ],
            options={
                'verbose_name_plural': 'endereços',
                'verbose_name': 'endereço',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('birthday', models.DateField(verbose_name='Aniversário')),
                ('address1', models.CharField(max_length=100, verbose_name='Endereço 1')),
                ('purchase_limit', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Limite de compra')),
            ],
            options={
                'verbose_name_plural': 'pessoas',
                'verbose_name': 'pessoa',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='persons.Person')),
                ('compra_sempre', models.BooleanField(default=False, verbose_name='Compra Sempre')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
                'verbose_name': 'Cliente',
            },
            bases=('persons.person',),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='persons.Person')),
                ('ctps', models.CharField(max_length=25, verbose_name='Carteira de Trabalho')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Salário')),
            ],
            options={
                'verbose_name_plural': 'Funcionários',
                'verbose_name': 'Funcionário',
            },
            bases=('persons.person',),
        ),
        migrations.AddField(
            model_name='address',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Person'),
        ),
    ]
