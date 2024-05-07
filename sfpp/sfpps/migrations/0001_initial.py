# Generated by Django 5.0.4 on 2024-05-05 00:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_ca', models.CharField(max_length=80, verbose_name='Nome Cartao')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cat', models.CharField(max_length=100, verbose_name='Nome')),
                ('descr_cat', models.TextField(verbose_name='Descriçao')),
            ],
        ),
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_mot', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pag', models.CharField(max_length=100, verbose_name='descricao')),
                ('descr_pag', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('valor_total', models.DecimalField(decimal_places=2, help_text='Valor total associado', max_digits=10, verbose_name='Valor total')),
                ('Data_pag', models.DateField(help_text='Data de vencimento ou pagamento', verbose_name='Data Pagamento')),
                ('pago', models.BooleanField(default=False)),
                ('mod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sfpps.modalidade')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sfpps.tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_gc', models.CharField(max_length=100, verbose_name='Nome')),
                ('data_gc', models.DateField(verbose_name='Data')),
                ('valor_gc', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('cartao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sfpps.cartao')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sfpps.categoria')),
                ('pagamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sfpps.pagamento')),
            ],
        ),
    ]
