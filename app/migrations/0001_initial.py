# Generated by Django 4.0.4 on 2022-05-14 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('sobrenome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('MG', 'Minas Gerais'), ('RJ', 'Rio de Janeiro'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('PA', 'Pará'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RO', 'Rondônia'), ('SE', 'Sergipe'), ('TO', 'Tocantins'), ('MS', 'Mato Grosso do Sul'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('AP', 'Amapá'), ('MT', 'Mato Grosso'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('RR', 'Roraima')], max_length=2)),
                ('celular', models.CharField(blank=True, max_length=9, null=True)),
            ],
        ),
    ]